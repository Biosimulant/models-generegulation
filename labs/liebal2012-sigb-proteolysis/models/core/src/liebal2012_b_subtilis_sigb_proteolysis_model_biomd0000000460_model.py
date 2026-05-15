# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Liebal2012 - B.subtilis sigB proteolysis model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Liebal2012BSubtilisSigbProteolysisModelBiomd0000000460Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1302080000'
    _TITLE = 'Liebal2012 - B.subtilis sigB proteolysis model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "sigb",
        "lacz",
        "x"
]
    _SPECIES_LABELS = {
        "lacz": "lacz",
        "sigb": "sigb",
        "x": "x"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {'iptg': ('IPTG', 100.0, 'native SBML value', 'Boundary species `IPTG`, the source induction level for this sigma-B model variant.')}
    _HEADLINE_OUTPUTS = {'sigma_b': ('sigb', 'native SBML value', 'sigb observable. Maps to SBML symbol `sigb`.'), 'lacz_reporter': ('lacz', 'native SBML value', 'lacz observable. Maps to SBML symbol `lacz`.'), 'model_state_x': ('x', 'native SBML value', 'x observable. Maps to SBML symbol `x`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000460.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
