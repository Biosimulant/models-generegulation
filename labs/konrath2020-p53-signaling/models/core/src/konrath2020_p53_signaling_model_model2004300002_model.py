# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Konrath2020_p53_signaling_model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Konrath2020P53SignalingModelModel2004300002Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Konrath2020_p53_subpopulation_a'
    _TITLE = 'Konrath2020_p53_signaling_model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "p53",
        "p53a",
        "Mdm2_mRNA",
        "Mdm2",
        "Wip1_mRNA",
        "Wip1",
        "pATM"
]
    _SPECIES_LABELS = {
        "Mdm2": "Mdm2",
        "Mdm2_mRNA": "Mdm2 mRNA",
        "Wip1": "Wip1",
        "Wip1_mRNA": "Wip1 mRNA",
        "p53": "p53",
        "p53a": "p53a",
        "pATM": "ATM P"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {'dna_damage_signal': ('damage', 1.0, 'native SBML value', 'Source parameter `damage`, used as the DNA-damage stimulus in the p53 signaling model.')}
    _HEADLINE_OUTPUTS = {'p53': ('p53', 'native SBML value', 'p53 observable. Maps to SBML symbol `p53`.'), 'active_p53': ('p53a', 'native SBML value', 'p53a observable. Maps to SBML symbol `p53a`.'), 'mdm2': ('Mdm2', 'native SBML value', 'Mdm2 observable. Maps to SBML symbol `Mdm2`.'), 'phosphorylated_atm': ('pATM', 'native SBML value', 'ATM P observable. Maps to SBML symbol `pATM`.')}

    def __init__(self, model_path: str = 'data/MODEL2004300002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
