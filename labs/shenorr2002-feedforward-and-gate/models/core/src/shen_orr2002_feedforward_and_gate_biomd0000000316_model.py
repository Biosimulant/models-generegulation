# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Shen-Orr2002_FeedForward_AND_gate."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class ShenOrr2002FeedforwardAndGateBiomd0000000316Model(TelluriumSBMLBioModule):
    _SBML_ID = 'shenorr02'
    _TITLE = 'Shen-Orr2002_FeedForward_AND_gate'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "Y",
        "Z"
]
    _SPECIES_LABELS = {
        "Y": "Y",
        "Z": "Z"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {'input_signal_x': ('X', 0.0, 'native SBML value', 'Boundary species `X`, the source upstream input to the coherent feed-forward loop.')}
    _HEADLINE_OUTPUTS = {'intermediate_regulator_y': ('Y', 'native SBML value', 'Y observable. Maps to SBML symbol `Y`.'), 'response_operon_z': ('Z', 'native SBML value', 'Z observable. Maps to SBML symbol `Z`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000316.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
