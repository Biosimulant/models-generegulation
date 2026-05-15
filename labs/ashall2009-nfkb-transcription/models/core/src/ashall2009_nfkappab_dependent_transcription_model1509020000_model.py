# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Ashall2009 - NFkappaB dependent transcription."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ashall2009NfkappabDependentTranscriptionModel1509020000Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1509020000'
    _TITLE = 'Ashall2009 - NFkappaB dependent transcription'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "species_1",
        "species_2",
        "species_3",
        "species_4",
        "species_5",
        "species_6",
        "species_7",
        "species_8",
        "species_9",
        "species_10",
        "species_11",
        "species_12",
        "species_13",
        "species_14"
]
    _SPECIES_LABELS = {
        "species_1": "IkBa",
        "species_10": "A20",
        "species_11": "tA20",
        "species_12": "nIkBa",
        "species_13": "nIkBa nNF-kB",
        "species_14": "nNF-kB",
        "species_2": "IkBa NF-kB",
        "species_3": "NF-kB",
        "species_4": "tIkBa",
        "species_5": "IKKa",
        "species_6": "pIkBa",
        "species_7": "pIkBa NF-kB",
        "species_8": "IKKn",
        "species_9": "IKKi"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'nuclear_nfkb': ('species_14', 'native SBML value', 'nNF-kB observable. Maps to SBML symbol `species_14`.'), 'nfkb': ('species_3', 'native SBML value', 'NF-kB observable. Maps to SBML symbol `species_3`.'), 'ikba_transcript': ('species_4', 'native SBML value', 'tIkBa observable. Maps to SBML symbol `species_4`.'), 'a20_transcript': ('species_11', 'native SBML value', 'tA20 observable. Maps to SBML symbol `species_11`.')}

    def __init__(self, model_path: str = 'data/MODEL1509020000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
