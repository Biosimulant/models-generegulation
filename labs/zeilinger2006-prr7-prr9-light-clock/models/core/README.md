# Zeilinger2006_PRR7-PRR9light-Yprime

The model reproduces the time profile of TOC1 and Y mRNA for a 8:16 cycle as depicted in Fig7A and 7B. A simple algorithm in the event section accomplishes the 8 hour light and 16 hour dark cycle.

This core model executes the bundled SBML file in `data/` through `TelluriumSBMLBioModule`. The SBML file remains the scientific source of truth; this wrapper only declares Biosimulant metadata, friendly ports, and traceable mappings.

No public biological inputs are exposed; no source-backed external control was validated for this lab.
