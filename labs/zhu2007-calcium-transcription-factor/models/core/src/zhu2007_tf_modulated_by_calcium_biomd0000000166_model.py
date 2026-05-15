# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Zhu2007_TF_modulated_by_Calcium."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zhu2007TfModulatedByCalciumBiomd0000000166Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Zhu2007_TF_syn_modulated_by_Ca'
    _TITLE = 'Zhu2007_TF_modulated_by_Calcium'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "X",
        "Y",
        "Z"
]
    _SPECIES_LABELS = {
        "X": "TF A",
        "Y": "Calcium in store",
        "Z": "Calcium in cytoplasm"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'active_transcription_factor': ('X', 'native SBML value', 'TF A observable. Maps to SBML symbol `X`.'), 'stored_calcium': ('Y', 'native SBML value', 'Calcium in store observable. Maps to SBML symbol `Y`.'), 'cytoplasmic_calcium': ('Z', 'native SBML value', 'Calcium in cytoplasm observable. Maps to SBML symbol `Z`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000166.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
