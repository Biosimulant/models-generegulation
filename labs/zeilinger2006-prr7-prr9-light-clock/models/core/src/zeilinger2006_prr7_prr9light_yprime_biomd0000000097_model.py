# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Zeilinger2006_PRR7-PRR9light-Yprime."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zeilinger2006Prr7Prr9lightYprimeBiomd0000000097Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Zeilinger2006_PRR7_PRR9light_Yprime'
    _TITLE = 'Zeilinger2006_PRR7-PRR9light-Yprime'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "cLc",
        "cLm",
        "cLn",
        "cP7c",
        "cP7m",
        "cP7n",
        "cP9c",
        "cP9m",
        "cP9n",
        "cPn",
        "cTc",
        "cTm",
        "cTn",
        "cXc",
        "cXm",
        "cXn",
        "cYc",
        "cYm",
        "cYn"
]
    _SPECIES_LABELS = {
        "cLc": "cLc",
        "cLm": "cLm",
        "cLn": "cLn",
        "cP7c": "cP7c",
        "cP7m": "cP7m",
        "cP7n": "cP7n",
        "cP9c": "cP9c",
        "cP9m": "cP9m",
        "cP9n": "cP9n",
        "cPn": "cPn",
        "cTc": "cTc",
        "cTm": "cTm",
        "cTn": "cTn",
        "cXc": "cXc",
        "cXm": "cXm",
        "cXn": "cXn",
        "cYc": "cYc",
        "cYm": "cYm",
        "cYn": "cYn"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'toc1_messenger_rna': ('cTm', 'native SBML value', 'cTm observable. Maps to SBML symbol `cTm`.'), 'nuclear_y': ('cYn', 'native SBML value', 'cYn observable. Maps to SBML symbol `cYn`.'), 'prr7_messenger_rna': ('cP7m', 'native SBML value', 'cP7m observable. Maps to SBML symbol `cP7m`.'), 'prr9_messenger_rna': ('cP9m', 'native SBML value', 'cP9m observable. Maps to SBML symbol `cP9m`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000097.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
