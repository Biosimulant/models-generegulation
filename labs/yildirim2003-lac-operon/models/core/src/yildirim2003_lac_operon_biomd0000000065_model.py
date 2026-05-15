# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Yildirim2003_Lac_Operon."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yildirim2003LacOperonBiomd0000000065Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Yildirim2003_Lac_operon'
    _TITLE = 'Yildirim2003_Lac_Operon'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "M",
        "B",
        "A",
        "L",
        "P",
        "I1",
        "I2",
        "I3"
]
    _SPECIES_LABELS = {
        "A": "allolactose",
        "B": "Betagalactosidase",
        "I1": "PartialmRNA",
        "I2": "PartialBetagalactosidase",
        "I3": "PartialPermease",
        "L": "lactose internal",
        "M": "mRNA",
        "P": "permease"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {'external_lactose': ('L_e', 0.08, 'native SBML value', 'Boundary species `L_e` (`External_Lactose`), the source extracellular lactose level.')}
    _HEADLINE_OUTPUTS = {'lac_messenger_rna': ('M', 'native SBML value', 'mRNA observable. Maps to SBML symbol `M`.'), 'beta_galactosidase': ('B', 'native SBML value', 'Betagalactosidase observable. Maps to SBML symbol `B`.'), 'allolactose': ('A', 'native SBML value', 'allolactose observable. Maps to SBML symbol `A`.'), 'permease': ('P', 'native SBML value', 'permease observable. Maps to SBML symbol `P`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000065.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
