# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Rantasalo2016 - Synthetic expresion modulator induced STF_B42."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rantasalo2016SyntheticExpresionModulatorInduModel1510230004Model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1510230004'
    _TITLE = 'Rantasalo2016 - Synthetic expresion modulator induced STF_B42'
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
        "MetTF_BTF",
        "MetTF",
        "Met",
        "DTF",
        "BTF",
        "B",
        "Met_MetTF",
        "Pol_TFn_B_CP2"
]
    _SPECIES_LABELS = {
        "B": "B",
        "BTF": "BTF",
        "CP": "CP",
        "DTF": "DTF",
        "MTFc": "MTFc",
        "Met": "Met",
        "MetTF": "MetTF",
        "MetTF_BTF": "MetTF:BTF",
        "Met_MetTF": "Met:MetTF",
        "MmCherryc": "MmCherryc",
        "Pol": "Pol",
        "Pol_DTF": "Pol:DTF",
        "Pol_TFn_B": "Pol:TFn:B",
        "Pol_TFn_B_CP2": "Pol:TFn:B:CP2",
        "TFc": "TFc",
        "TFn": "TFn",
        "TFn_B": "TFn:B",
        "mCherryc": "mCherryc"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'mcherry_messenger_rna': ('MmCherryc', 'native SBML value', 'MmCherryc observable. Maps to SBML symbol `MmCherryc`.'), 'mcherry_reporter': ('mCherryc', 'native SBML value', 'mCherryc observable. Maps to SBML symbol `mCherryc`.'), 'cytosolic_transcription_factor': ('TFc', 'native SBML value', 'TFc observable. Maps to SBML symbol `TFc`.'), 'met_transcription_factor': ('MetTF', 'native SBML value', 'MetTF observable. Maps to SBML symbol `MetTF`.')}

    def __init__(self, model_path: str = 'data/MODEL1510230004.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
