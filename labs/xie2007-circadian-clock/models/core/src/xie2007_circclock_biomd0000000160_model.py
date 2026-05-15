# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Xie2007_CircClock."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Xie2007CircclockBiomd0000000160Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Xie2007_CircClock'
    _TITLE = 'Xie2007_CircClock'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "CC",
        "CCPT",
        "clkp",
        "perp",
        "clkm",
        "perm",
        "PT",
        "vrip",
        "vrim",
        "VRI",
        "pdpp",
        "pdpm",
        "PDP",
        "CLK",
        "PER",
        "timp",
        "timm",
        "TIM",
        "prcper",
        "prcv",
        "prcpdp",
        "prvc",
        "prpc",
        "prct"
]
    _SPECIES_LABELS = {
        "CC": "CC",
        "CCPT": "CCPT",
        "CLK": "CLK",
        "PDP": "PDP",
        "PER": "PER",
        "PT": "PT",
        "TIM": "TIM",
        "VRI": "VRI",
        "clkm": "clkm",
        "clkp": "clkp",
        "pdpm": "pdpm",
        "pdpp": "pdpp",
        "perm": "perm",
        "perp": "perp",
        "prcpdp": "CCbindingpdp",
        "prcper": "CCbindingPer",
        "prct": "CCbindingtim",
        "prcv": "CCbindingvri",
        "prpc": "PDPbindingclkp",
        "prvc": "VRIbindingclkp",
        "timm": "timm",
        "timp": "timp",
        "vrim": "vrim",
        "vrip": "vrip"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'period_protein': ('PER', 'native SBML value', 'PER observable. Maps to SBML symbol `PER`.'), 'timeless_protein': ('TIM', 'native SBML value', 'TIM observable. Maps to SBML symbol `TIM`.'), 'clock_protein': ('CLK', 'native SBML value', 'CLK observable. Maps to SBML symbol `CLK`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000160.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
