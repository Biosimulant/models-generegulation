# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Koster1988_Histone_Expression."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Koster1988HistoneExpressionModel5954483266Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL5954483266'
    _TITLE = 'Koster1988_Histone_Expression'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "RNA",
        "Prot"
]
    _SPECIES_LABELS = {
        "Prot": "H3 Protein",
        "RNA": "H3 RNA"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'histone_rna': ('RNA', 'native SBML value', 'H3 RNA observable. Maps to SBML symbol `RNA`.'), 'histone_protein': ('Prot', 'native SBML value', 'H3 Protein observable. Maps to SBML symbol `Prot`.')}

    def __init__(self, model_path: str = 'data/MODEL5954483266.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
