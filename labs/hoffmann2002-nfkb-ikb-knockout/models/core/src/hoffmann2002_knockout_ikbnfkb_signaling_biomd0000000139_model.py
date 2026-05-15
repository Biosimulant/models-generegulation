# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Hoffmann2002_KnockOut_IkBNFkB_Signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hoffmann2002KnockoutIkbnfkbSignalingBiomd0000000139Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Hoffmann2002_KnockOut_IkBNFkB_Signaling'
    _TITLE = 'Hoffmann2002_KnockOut_IkBNFkB_Signaling'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "IkBalpha",
        "NFkB",
        "IkBalpha_NFkB",
        "IkBbeta",
        "IkBbeta_NFkB",
        "IkBeps",
        "IkBeps_NFkB",
        "IKK_IkBalpha",
        "IKK_IkBalpha_NFkB",
        "IKK",
        "IKK_IkBbeta",
        "IKK_IkBbeta_NFkB",
        "IKK_IkBeps",
        "IKK_IkBeps_NFkB",
        "NFkB_nuc",
        "IkBalpha_nuc",
        "IkBalpha_nuc_NFkB_nuc",
        "IkBbeta_nuc",
        "IkBbeta_nuc_NFkB_nuc",
        "IkBeps_nuc",
        "IkBalpha_transcript",
        "IkBbeta_transcript",
        "IkBeps_transcript",
        "IkBeps_nuc_NFkB_nuc"
]
    _SPECIES_LABELS = {
        "IKK": "IKK",
        "IKK_IkBalpha": "IKK IkBalpha",
        "IKK_IkBalpha_NFkB": "IKK IkBalpha NF-kB",
        "IKK_IkBbeta": "IKK IkBbeta",
        "IKK_IkBbeta_NFkB": "IKK IkBbeta NF-kB",
        "IKK_IkBeps": "IKK IkBeps",
        "IKK_IkBeps_NFkB": "IKK IkBeps NF-kB",
        "IkBalpha": "IkBalpha",
        "IkBalpha_NFkB": "IkBalpha NF-kB",
        "IkBalpha_nuc": "IkBalpha nuc",
        "IkBalpha_nuc_NFkB_nuc": "IkBalpha nuc NF-kB nuc",
        "IkBalpha_transcript": "IkBalpha transcript",
        "IkBbeta": "IkBbeta",
        "IkBbeta_NFkB": "IkBbeta NF-kB",
        "IkBbeta_nuc": "IkBbeta nuc",
        "IkBbeta_nuc_NFkB_nuc": "IkBbeta nuc NF-kB nuc",
        "IkBbeta_transcript": "IkBbeta transcript",
        "IkBeps": "IkBeps",
        "IkBeps_NFkB": "IkBeps NF-kB",
        "IkBeps_nuc": "IkBeps nuc",
        "IkBeps_nuc_NFkB_nuc": "IkBeps nuc NF-kB nuc",
        "IkBeps_transcript": "IkBeps transcript",
        "NFkB": "NF-kB",
        "NFkB_nuc": "NF-kB nuc"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'nfkb': ('NFkB', 'native SBML value', 'NF-kB observable. Maps to SBML symbol `NFkB`.'), 'ikb_alpha': ('IkBalpha', 'native SBML value', 'IkBalpha observable. Maps to SBML symbol `IkBalpha`.'), 'ikk': ('IKK', 'native SBML value', 'IKK observable. Maps to SBML symbol `IKK`.'), 'ikb_alpha_nfkb_complex': ('IkBalpha_NFkB', 'native SBML value', 'IkBalpha NF-kB observable. Maps to SBML symbol `IkBalpha_NFkB`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000139.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
