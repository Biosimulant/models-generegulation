# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Linke2017 - Synchronization of Cyclins' expression by the Fkh2 transcription factor in the budding yeast cell cycle."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Linke2017SynchronizationOfCyclinsExpressionBiomd0000000934Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Linke2017___Synchronization_of_Cyclins__expression_by_the_Fkh2_transcription_factor_in_the_budding_yeast_cell_cycle'
    _TITLE = "Linke2017 - Synchronization of Cyclins' expression by the Fkh2 transcription factor in the budding yeast cell cycle"
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "Sic1",
        "Cdk1_Clb5or6",
        "Cdk1_Clb5or6_Sic1",
        "Clb5or6_degraded",
        "Cdk1_Clb3or4",
        "Cdk1_Clb3or4_Sic1",
        "Clb3or4_degraded",
        "Cdk1_Clb1or2",
        "Cdk1_Clb1or2_Sic1",
        "Clb1or2_degraded",
        "Sic1_degraded_re14",
        "Sic1_degraded_re18",
        "Sic1_degraded_re5"
]
    _SPECIES_LABELS = {
        "Cdk1_Clb1or2": "Cdk1 Clb1or2",
        "Cdk1_Clb1or2_Sic1": "Cdk1 Clb1or2 Sic1",
        "Cdk1_Clb3or4": "Cdk1 Clb3or4",
        "Cdk1_Clb3or4_Sic1": "Cdk1 Clb3or4 Sic1",
        "Cdk1_Clb5or6": "Cdk1 Clb5or6",
        "Cdk1_Clb5or6_Sic1": "Cdk1 Clb5or6 Sic1",
        "Clb1or2_degraded": "Clb1or2 degraded",
        "Clb3or4_degraded": "Clb3or4 degraded",
        "Clb5or6_degraded": "Clb5or6 degraded",
        "Sic1": "Sic1",
        "Sic1_degraded_re14": "Sic1 degraded re14",
        "Sic1_degraded_re18": "Sic1 degraded re18",
        "Sic1_degraded_re5": "Sic1 degraded re5"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'sic1': ('Sic1', 'native SBML value', 'Sic1 observable. Maps to SBML symbol `Sic1`.'), 'cdk1_clb5_or_clb6': ('Cdk1_Clb5or6', 'native SBML value', 'Cdk1 Clb5or6 observable. Maps to SBML symbol `Cdk1_Clb5or6`.'), 'cdk1_clb3_or_clb4': ('Cdk1_Clb3or4', 'native SBML value', 'Cdk1 Clb3or4 observable. Maps to SBML symbol `Cdk1_Clb3or4`.'), 'cdk1_clb1_or_clb2': ('Cdk1_Clb1or2', 'native SBML value', 'Cdk1 Clb1or2 observable. Maps to SBML symbol `Cdk1_Clb1or2`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000934.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
