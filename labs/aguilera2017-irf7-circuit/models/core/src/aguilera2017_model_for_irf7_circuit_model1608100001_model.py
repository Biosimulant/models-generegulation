# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Aguilera2017 - Model for IRF7 circuit."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Aguilera2017ModelForIrf7CircuitModel1608100001Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1608100001'
    _TITLE = 'Aguilera2017 - Model for IRF7 circuit'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "Pa",
        "ISGF3",
        "IRF7",
        "IRF7phosp",
        "IRF7dimer",
        "mRNA",
        "IFN"
]
    _SPECIES_LABELS = {
        "IFN": "IFN",
        "IRF7": "IRF7",
        "IRF7dimer": "IRF7dimer",
        "IRF7phosp": "IRF7phosp",
        "ISGF3": "ISGF3",
        "Pa": "Pa",
        "mRNA": "mRNA"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'irf7': ('IRF7', 'native SBML value', 'IRF7 observable. Maps to SBML symbol `IRF7`.'), 'phosphorylated_irf7': ('IRF7phosp', 'native SBML value', 'IRF7phosp observable. Maps to SBML symbol `IRF7phosp`.'), 'irf7_dimer': ('IRF7dimer', 'native SBML value', 'IRF7dimer observable. Maps to SBML symbol `IRF7dimer`.'), 'interferon': ('IFN', 'native SBML value', 'IFN observable. Maps to SBML symbol `IFN`.')}

    def __init__(self, model_path: str = 'data/MODEL1608100001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
