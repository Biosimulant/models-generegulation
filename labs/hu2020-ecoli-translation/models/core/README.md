# Hu2020 - E. coli translation model

This translation model consists of 274 biochemical reactions, including 119 reactions with non-linear kinetics. This mechanistic model accounts for the concentrations of mRNA, the ribosome, the differ.

This core model executes the bundled SBML file in `data/` through `TelluriumSBMLBioModule`. The SBML file remains the scientific source of truth; this wrapper only declares Biosimulant metadata, friendly ports, and traceable mappings.

No public biological inputs are exposed; no source-backed external control was validated for this lab.
