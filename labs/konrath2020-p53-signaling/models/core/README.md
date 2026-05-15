# Konrath2020_p53_signaling_model

The ODE model is based on Batchelor et al., Mol. It can be used to explore generegulation konrath2020 p53 signaling model2004300002 dynamics and compare simulation behavior across conditions.

This core model executes the bundled SBML file in `data/` through `TelluriumSBMLBioModule`. The SBML file remains the scientific source of truth; this wrapper only declares Biosimulant metadata, friendly ports, and traceable mappings.

Validated public inputs: dna_damage_signal
