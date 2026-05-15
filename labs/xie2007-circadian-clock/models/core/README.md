# Xie2007_CircClock

The model reproduces the oscillations for mRNA and protein species as depicted in Fig 3 of the plot. The model differs slightly from that given in the paper and this was made after a communication fro.

This core model executes the bundled SBML file in `data/` through `TelluriumSBMLBioModule`. The SBML file remains the scientific source of truth; this wrapper only declares Biosimulant metadata, friendly ports, and traceable mappings.

No public biological inputs are exposed; no source-backed external control was validated for this lab.
