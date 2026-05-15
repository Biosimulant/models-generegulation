# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Koo2013 - Shear stress induced eNOS expression - Model 3."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koo2013ShearStressInducedEnosExpressionModBiomd0000000466Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1302180005'
    _TITLE = 'Koo2013 - Shear stress induced eNOS expression - Model 3'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "s35",
        "s37",
        "s38",
        "s39",
        "s42",
        "s43",
        "s44",
        "s49",
        "s51",
        "s91",
        "s92",
        "s93",
        "s94",
        "s95",
        "s96",
        "s97",
        "s98",
        "s99",
        "s100",
        "s101",
        "s102",
        "s103",
        "s104",
        "s105",
        "s106",
        "s107",
        "s108",
        "s110",
        "s111",
        "s112",
        "s113",
        "s114",
        "s115",
        "s119"
]
    _SPECIES_LABELS = {
        "s100": "p JNKK",
        "s101": "p MEKK1",
        "s102": "Ras:GTP",
        "s103": "Ras:GDP",
        "s104": "p JNK",
        "s105": "KLF2",
        "s106": "eNOS",
        "s107": "aAP 1",
        "s108": "eNOS",
        "s110": "p FAK:Shc",
        "s111": "Grb2:Sos",
        "s112": "p FAK:p Shc",
        "s113": "p FAK:p Shc:Grb2:Sos",
        "s114": "p Shc:Grb2:Sos",
        "s115": "eNOS",
        "s119": "Shear Stress",
        "s35": "s35",
        "s37": "s37",
        "s38": "pre time",
        "s39": "Time",
        "s42": "AP 1",
        "s43": "pp JNKK",
        "s44": "pp JNK",
        "s49": "KLF2",
        "s51": "eNOS Cav 1",
        "s91": "Shc",
        "s92": "p Src",
        "s93": "p FAK",
        "s94": "Src",
        "s95": "FAK",
        "s96": "JNKK",
        "s97": "MEKK1",
        "s98": "p Shc",
        "s99": "JNK"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'enos': ('s106', 'native SBML value', 'eNOS observable. Maps to SBML symbol `s106`.'), 'klf2': ('s49', 'native SBML value', 'KLF2 observable. Maps to SBML symbol `s49`.'), 'ap1': ('s42', 'native SBML value', 'AP 1 observable. Maps to SBML symbol `s42`.'), 'active_ras': ('s102', 'native SBML value', 'Ras:GTP observable. Maps to SBML symbol `s102`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000466.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
