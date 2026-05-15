# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Aguilera2017 - Model for gene constitutive expression circuit."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Aguilera2017ModelForGeneConstitutiveExpressModel1608100000Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1608100000'
    _TITLE = 'Aguilera2017 - Model for gene constitutive expression circuit'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "mRNA",
        "Protein"
]
    _SPECIES_LABELS = {
        "Protein": "Protein",
        "mRNA": "mRNA"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'messenger_rna': ('mRNA', 'native SBML value', 'mRNA observable. Maps to SBML symbol `mRNA`.'), 'protein': ('Protein', 'native SBML value', 'Protein observable. Maps to SBML symbol `Protein`.')}

    def __init__(self, model_path: str = 'data/MODEL1608100000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
