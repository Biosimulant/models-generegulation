# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Cao2010 - Epigenetic state of lysogeny in phage lambda."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cao2010EpigeneticStateOfLysogenyInPhageLaModel1308080003Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1308080003'
    _TITLE = 'Cao2010 - Epigenetic state of lysogeny in phage lambda'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "OR1",
        "OR2",
        "OR3",
        "CI",
        "Cro",
        "CI2",
        "Cro2",
        "ROR1",
        "ROR2",
        "ROR3",
        "COR1",
        "COR2",
        "COR3",
        "EmptySet"
]
    _SPECIES_LABELS = {
        "CI": "pCI",
        "CI2": "R2",
        "COR1": "COR1",
        "COR2": "COR2",
        "COR3": "COR3",
        "Cro": "pCro",
        "Cro2": "C2",
        "EmptySet": "EmptySet",
        "OR1": "OR1",
        "OR2": "OR2",
        "OR3": "OR3",
        "ROR1": "ROR1",
        "ROR2": "ROR2",
        "ROR3": "ROR3"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'ci_repressor': ('CI', 'native SBML value', 'pCI observable. Maps to SBML symbol `CI`.'), 'cro_repressor': ('Cro', 'native SBML value', 'pCro observable. Maps to SBML symbol `Cro`.'), 'ci_dimer': ('CI2', 'native SBML value', 'R2 observable. Maps to SBML symbol `CI2`.'), 'cro_dimer': ('Cro2', 'native SBML value', 'C2 observable. Maps to SBML symbol `Cro2`.')}

    def __init__(self, model_path: str = 'data/MODEL1308080003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
