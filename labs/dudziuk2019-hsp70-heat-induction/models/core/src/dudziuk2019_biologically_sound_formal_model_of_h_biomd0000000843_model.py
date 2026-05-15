# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Dudziuk2019 - Biologically sound formal model of Hsp70 heat induction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dudziuk2019BiologicallySoundFormalModelOfHBiomd0000000843Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Dudziuk2019___Biologically_sound_formal_model_of_Hsp70_heat_induction'
    _TITLE = 'Dudziuk2019 - Biologically sound formal model of Hsp70 heat induction'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "HSP",
        "HSF",
        "S",
        "HSP_HSF",
        "HSP_S",
        "HSF_3",
        "HSE",
        "HSE_HSF_3",
        "P",
        "mRNA"
]
    _SPECIES_LABELS = {
        "HSE": "HSE",
        "HSE_HSF_3": "HSE HSF 3",
        "HSF": "HSF",
        "HSF_3": "HSF 3",
        "HSP": "HSP",
        "HSP_HSF": "HSP HSF",
        "HSP_S": "HSP S",
        "P": "P",
        "S": "S",
        "mRNA": "mRNA"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'heat_shock_protein': ('HSP', 'native SBML value', 'HSP observable. Maps to SBML symbol `HSP`.'), 'heat_shock_factor': ('HSF', 'native SBML value', 'HSF observable. Maps to SBML symbol `HSF`.'), 'hsp70_messenger_rna': ('mRNA', 'native SBML value', 'mRNA observable. Maps to SBML symbol `mRNA`.'), 'protein_product': ('P', 'native SBML value', 'P observable. Maps to SBML symbol `P`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000843.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
