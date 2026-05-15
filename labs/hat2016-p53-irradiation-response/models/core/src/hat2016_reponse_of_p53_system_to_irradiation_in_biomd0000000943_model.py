# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Hat2016 - Reponse of p53 System to irradiation in cell fate decision making."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hat2016ReponseOfP53SystemToIrradiationInBiomd0000000943Model(TelluriumSBMLBioModule):
    _SBML_ID = 'Hat2016___Reponse_of_p53_System_to_irradiation_in_cell_fate_decision_making'
    _TITLE = 'Hat2016 - Reponse of p53 System to irradiation in cell fate decision making'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = "species"
    _OBSERVABLES = [
        "DNA_double_strand_break",
        "ATM_phosphorylated",
        "SIAH1_0",
        "HIPK2",
        "p53_0phosphorylated",
        "p53_arrester",
        "p53_S46phosphorylated",
        "Mdm2_nuc_S166S186phosphorylated",
        "Wip1",
        "p53_killer",
        "Mdm2_mRNA",
        "Mdm2_cyt_0phosphorylated",
        "Mdm2_cyt_S166S186phosphorylated",
        "AKT_phosphorylated",
        "Mdm2_nuc_S166S186p_S395p",
        "Wip1_mRNA",
        "PTEN_mRNA",
        "PTEN",
        "PIP3",
        "p21_mRNA",
        "p21__free",
        "Cyclin_E__free",
        "Cyclin_E_p21_complex",
        "Rb1_0__free",
        "Rb1_0_E2F1_complex",
        "Bax_mRNA",
        "Bax__free",
        "BclXL__free",
        "Bax_BclXL_complex",
        "Bad_0__free",
        "Bad_phosphorylated__free",
        "proCaspase",
        "Caspase"
]
    _SPECIES_LABELS = {
        "AKT_phosphorylated": "AKT phosphorylated",
        "ATM_phosphorylated": "ATM phosphorylated",
        "Bad_0__free": "Bad 0 (free)",
        "Bad_phosphorylated__free": "Bad phosphorylated (free)",
        "Bax_BclXL_complex": "Bax:BclXL complex",
        "Bax__free": "Bax (free)",
        "Bax_mRNA": "Bax mRNA",
        "BclXL__free": "BclXL (free)",
        "Caspase": "Caspase",
        "Cyclin_E__free": "Cyclin E (free)",
        "Cyclin_E_p21_complex": "Cyclin E:p21 complex",
        "DNA_double_strand_break": "DNA double strand break",
        "HIPK2": "HIPK2",
        "Mdm2_cyt_0phosphorylated": "Mdm2 cyt 0phosphorylated",
        "Mdm2_cyt_S166S186phosphorylated": "Mdm2 cyt S166S186phosphorylated",
        "Mdm2_mRNA": "Mdm2 mRNA",
        "Mdm2_nuc_S166S186p_S395p": "Mdm2 nuc S166S186p S395p",
        "Mdm2_nuc_S166S186phosphorylated": "Mdm2 nuc S166S186phosphorylated",
        "PIP3": "PIP3",
        "PTEN": "PTEN",
        "PTEN_mRNA": "PTEN mRNA",
        "Rb1_0_E2F1_complex": "Rb1 0:E2F1 complex",
        "Rb1_0__free": "Rb1 0 (free)",
        "SIAH1_0": "SIAH1 0",
        "Wip1": "Wip1",
        "Wip1_mRNA": "Wip1 mRNA",
        "p21__free": "p21 (free)",
        "p21_mRNA": "p21 mRNA",
        "p53_0phosphorylated": "p53 0phosphorylated",
        "p53_S46phosphorylated": "p53 S46phosphorylated",
        "p53_arrester": "p53 arrester",
        "p53_killer": "p53 killer",
        "proCaspase": "proCaspase"
}
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {'dna_double_strand_breaks': ('DNA_double_strand_break', 'native SBML value', 'DNA double strand break observable. Maps to SBML symbol `DNA_double_strand_break`.'), 'p53_arrester': ('p53_arrester', 'native SBML value', 'p53 arrester observable. Maps to SBML symbol `p53_arrester`.'), 'p53_killer': ('p53_killer', 'native SBML value', 'p53 killer observable. Maps to SBML symbol `p53_killer`.'), 'mdm2_messenger_rna': ('Mdm2_mRNA', 'native SBML value', 'Mdm2 mRNA observable. Maps to SBML symbol `Mdm2_mRNA`.')}

    def __init__(self, model_path: str = 'data/BIOMD0000000943.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
