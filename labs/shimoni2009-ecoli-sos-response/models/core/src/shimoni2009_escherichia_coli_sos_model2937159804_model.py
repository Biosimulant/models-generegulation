# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Shimoni2009 - Escherichia Coli SOS."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shimoni2009EscherichiaColiSosModel2937159804Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2937159804'
    _TITLE = 'Shimoni2009 - Escherichia Coli SOS'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "bLexA",
        "mLexA",
        "LexA",
        "bRecA",
        "mRecA",
        "RecA",
        "bLexA",
        "mLexA",
        "LexA",
        "bRecA",
        "mRecA",
        "RecA"
]
    _SPECIES_LABELS = {
        "LexA": "LexA",
        "RecA": "RecA",
        "bLexA": "bLexA",
        "bRecA": "bRecA",
        "mLexA": "mLexA",
        "mRecA": "mRecA"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'lexa': ('LexA', 'native SBML value', 'LexA observable. Maps to SBML symbol `LexA`.'), 'reca': ('RecA', 'native SBML value', 'RecA observable. Maps to SBML symbol `RecA`.'), 'lexa_messenger_rna': ('mLexA', 'native SBML value', 'mLexA observable. Maps to SBML symbol `mLexA`.'), 'reca_messenger_rna': ('mRecA', 'native SBML value', 'mRecA observable. Maps to SBML symbol `mRecA`.')}

    def __init__(self, model_path: str = 'data/MODEL2937159804.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
