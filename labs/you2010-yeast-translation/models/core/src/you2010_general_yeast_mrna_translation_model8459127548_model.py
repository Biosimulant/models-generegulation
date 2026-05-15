# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for You2010_General_Yeast_mRNA_Translation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class You2010GeneralYeastMrnaTranslationModel8459127548Model(TelluriumSBMLBioModule):
    _SBML_ID = 'model'
    _TITLE = 'You2010_General_Yeast_mRNA_Translation'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "His_vac",
        "His_cyt",
        "Hts1",
        "HisAMPHts1",
        "tRNA_His",
        "HistRNA_His",
        "Gcn2",
        "Gcn2P",
        "eIF2GDP",
        "eIF2PGDP",
        "eIF2B",
        "eIF2BeIF2GDP",
        "eIF2BeIF2PGDP",
        "eIF2GTP",
        "TC",
        "eIF1",
        "eIF3",
        "eIF5",
        "TCeIF5",
        "eIF5eIF2GDP",
        "eIF1eIF3",
        "eIF3eIF5",
        "eIF1eIF3eIF5",
        "TCeIF5eIF3",
        "MFC",
        "MFCeIF5",
        "_40S",
        "_43S",
        "_40SmRNA",
        "RibosomemRNA"
]
    _SPECIES_LABELS = {
        "Gcn2": "Gcn2",
        "Gcn2P": "Gcn2(P)",
        "HisAMPHts1": "His AMP Hts1",
        "His_cyt": "His cyt",
        "His_vac": "His vac",
        "HistRNA_His": "His tRNA His",
        "Hts1": "Hts1",
        "MFC": "MFC",
        "MFCeIF5": "MFC eIF5",
        "RibosomemRNA": "Ribosome mRNA",
        "TC": "TC",
        "TCeIF5": "TC eIF5",
        "TCeIF5eIF3": "TC eIF5 eIF3",
        "_40S": "40S",
        "_40SmRNA": "40S mRNA",
        "_43S": "43S",
        "eIF1": "eIF1",
        "eIF1eIF3": "eIF1 eIF3",
        "eIF1eIF3eIF5": "eIF1 eIF3 eIF5",
        "eIF2B": "eIF2B",
        "eIF2BeIF2GDP": "eIF2B eIF2 GDP",
        "eIF2BeIF2PGDP": "eIF2B eIF2(P) GDP",
        "eIF2GDP": "eIF2 GDP",
        "eIF2GTP": "eIF2 GTP",
        "eIF2PGDP": "eIF2(P) GDP",
        "eIF3": "eIF3",
        "eIF3eIF5": "eIF3 eIF5",
        "eIF5": "eIF5",
        "eIF5eIF2GDP": "eIF5 eIF2 GDP",
        "tRNA_His": "tRNA His"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'eif2_gdp': ('eIF2GDP', 'native SBML value', 'eIF2 GDP observable. Maps to SBML symbol `eIF2GDP`.'), 'eif2b': ('eIF2B', 'native SBML value', 'eIF2B observable. Maps to SBML symbol `eIF2B`.'), 'initiation_complex_43s': ('_43S', 'native SBML value', '43S observable. Maps to SBML symbol `_43S`.'), 'ribosome_mrna_complex': ('RibosomemRNA', 'native SBML value', 'Ribosome mRNA observable. Maps to SBML symbol `RibosomemRNA`.')}

    def __init__(self, model_path: str = 'data/MODEL8459127548.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
