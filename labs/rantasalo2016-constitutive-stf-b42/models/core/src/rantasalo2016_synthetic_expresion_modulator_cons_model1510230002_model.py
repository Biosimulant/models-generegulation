# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Rantasalo2016 - Synthetic expresion modulator constitutive STF_B42."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rantasalo2016SyntheticExpresionModulatorConsModel1510230002Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1510230002'
    _TITLE = 'Rantasalo2016 - Synthetic expresion modulator constitutive STF_B42'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "MmCherryc",
        "mCherryc",
        "TFc",
        "MTFc",
        "Pol",
        "TFn_B",
        "CP",
        "Pol_TFn_B",
        "TFn",
        "Pol_DTF",
        "DTF",
        "B",
        "Pol_TFn_B_CP"
]
    _SPECIES_LABELS = {
        "B": "B",
        "CP": "CP",
        "DTF": "DTF",
        "MTFc": "MTFc",
        "MmCherryc": "MmCherryc",
        "Pol": "Pol",
        "Pol_DTF": "Pol:DTF",
        "Pol_TFn_B": "Pol:TFn:B",
        "Pol_TFn_B_CP": "Pol:TFn:B:CP",
        "TFc": "TFc",
        "TFn": "TFn",
        "TFn_B": "TFn:B",
        "mCherryc": "mCherryc"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'mcherry_messenger_rna': ('MmCherryc', 'native SBML value', 'MmCherryc observable. Maps to SBML symbol `MmCherryc`.'), 'mcherry_reporter': ('mCherryc', 'native SBML value', 'mCherryc observable. Maps to SBML symbol `mCherryc`.'), 'cytosolic_transcription_factor': ('TFc', 'native SBML value', 'TFc observable. Maps to SBML symbol `TFc`.'), 'nuclear_transcription_factor': ('TFn', 'native SBML value', 'TFn observable. Maps to SBML symbol `TFn`.')}

    def __init__(self, model_path: str = 'data/MODEL1510230002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
