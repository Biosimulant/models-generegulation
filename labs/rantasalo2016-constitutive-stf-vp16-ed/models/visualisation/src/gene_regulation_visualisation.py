# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Gene-regulation visualisation model."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import BioSignal, SignalSpec, unwrap_payload


def _value(signal: BioSignal | None) -> Any:
    return unwrap_payload(signal) if signal is not None else None


def _number(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if number == number and number not in (float("inf"), float("-inf")) else None


class GeneRegulationVisualisationModel(BioModule):
    def __init__(
        self,
        *,
        lab_title: str,
        question: str,
        answer_focus: str,
        caveat: str,
        alias: str,
        observables: list[dict[str, str]],
        state_observables: list[str],
        species_label_ids: list[str],
        integration_step: float = 1.0,
    ) -> None:
        self.lab_title = lab_title
        self.question = question
        self.answer_focus = answer_focus
        self.caveat = caveat
        self.alias = alias
        self.observables = list(observables)
        self.state_observables = list(state_observables)
        self.species_label_ids = list(species_label_ids)
        self.integration_step = float(integration_step)
        self._inputs: dict[str, BioSignal] = {}
        self._history: list[dict[str, float]] = []
        self._last_summary: Mapping[str, Any] = {}
        self._labels: Mapping[str, str] = {}

    def inputs(self) -> dict[str, SignalSpec]:
        scalar = SignalSpec.scalar(dtype="float64", description="Headline observable from the core model.")
        state_schema = {name: "float" for name in self.state_observables} or {"payload": "json"}
        species_label_schema = {name: "str" for name in self.species_label_ids} or {"payload": "json"}
        summary_schema = {
            "duration_simulated": "float",
            "observable_count": "int",
            "largest_change_observable": "str",
            "largest_change_magnitude": "float",
            "peak_observable": "str",
            "peak_value": "float",
        }
        return {
            f"{self.alias}_state": SignalSpec.record(
                schema=state_schema,
                description="Full core SBML state.",
            ),
            f"{self.alias}_summary": SignalSpec.record(
                schema=summary_schema,
                description="Core model summary.",
            ),
            f"{self.alias}_species_labels": SignalSpec.record(
                schema=species_label_schema,
                description="Core species labels.",
            ),
            **{f"{self.alias}_{item['port']}": scalar for item in self.observables},
        }

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self._history = []
        self._last_summary = {}
        self._labels = {}

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        self._inputs = dict(inputs or {})

    def advance_window(self, start: float, end: float) -> None:
        row: dict[str, float] = {"t": float(end)}
        state = _value(self._inputs.get(f"{self.alias}_state"))
        if isinstance(state, Mapping):
            for item in self.observables:
                number = _number(state.get(item["id"]))
                if number is not None:
                    row[item["id"]] = number
        for item in self.observables:
            number = _number(_value(self._inputs.get(f"{self.alias}_{item['port']}")))
            if number is not None:
                row[item["id"]] = number
        summary = _value(self._inputs.get(f"{self.alias}_summary"))
        if isinstance(summary, Mapping):
            self._last_summary = summary
        labels = _value(self._inputs.get(f"{self.alias}_species_labels"))
        if isinstance(labels, Mapping):
            self._labels = labels
        if len(row) > 1:
            self._history.append(row)

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> Optional[list[dict[str, Any]]]:
        if not self._history:
            return [
                {
                    "render": "table",
                    "description": "Direct scientific answer for this lab run.",
                    "data": {
                        "title": f"{self.lab_title} - run interpretation",
                        "columns": ["Prompt", "Answer"],
                        "rows": [
                            ["Scientific question", self.question],
                            ["Observed answer", "No renderable state has been received yet."],
                            ["Evidence", "The visualisation model has not captured any numeric core outputs."],
                            ["Dominant module", self.answer_focus],
                            ["Caveat", self.caveat],
                        ],
                    },
                }
            ]
        latest = self._history[-1]
        observed = [item for item in self.observables if item["id"] in latest]
        final_items = [
            {"label": item["label"], "value": float(latest[item["id"]])}
            for item in observed
            if _number(latest.get(item["id"])) is not None
        ]
        largest = str(self._last_summary.get("largest_change_observable") or "")
        peak = str(self._last_summary.get("peak_observable") or "")
        largest_label = self._labels.get(largest, largest) if largest else "none"
        peak_label = self._labels.get(peak, peak) if peak else "none"
        if final_items:
            dominant = max(final_items, key=lambda item: abs(float(item["value"])))
            answer = f"{dominant['label']} has the largest final magnitude among the curated outputs."
        else:
            dominant = {"label": "none", "value": 0.0}
            answer = "The curated outputs were finite but no final-value bar could be constructed."
        visuals: list[dict[str, Any]] = [
            {
                "render": "table",
                "description": "Direct scientific answer for this lab run.",
                "data": {
                    "title": f"{self.lab_title} - run interpretation",
                    "columns": ["Prompt", "Answer"],
                    "rows": [
                        ["Scientific question", self.question],
                        ["Observed answer", answer],
                        ["Evidence", f"Largest changing observable: {largest_label}; peak observable: {peak_label}."],
                        ["Dominant module", self.answer_focus],
                        ["Caveat", self.caveat],
                    ],
                },
            }
        ]
        series = []
        for item in observed:
            points = [[float(row["t"]), float(row[item["id"]])] for row in self._history if item["id"] in row]
            if points:
                series.append({"name": item["label"], "points": points})
        if series:
            visuals.append(
                {
                    "render": "timeseries",
                    "description": self.answer_focus,
                    "data": {
                        "title": f"{self.lab_title} - selected observables",
                        "x_label": "Model time",
                        "y_label": "Native SBML value",
                        "series": series,
                    },
                }
            )
        if final_items:
            visuals.append(
                {
                    "render": "bar",
                    "description": "Final values for the curated gene-regulation observables.",
                    "data": {
                        "title": f"{self.lab_title} - final state",
                        "items": final_items,
                    },
                }
            )
        return visuals
