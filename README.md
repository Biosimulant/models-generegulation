# models-generegulation

Curated collection of **gene regulation** simulation models for the **biosim** platform. This repository contains computational models of transcriptional regulation, gene regulatory networks, transcription factor dynamics, epigenetic control, and post-transcriptional regulation including miRNA and mRNA translation.

## What's Inside

### Models (43 packages)

Each model is a self-contained simulation component with a `model.yaml` manifest, covering diverse aspects of gene regulation from transcription factors to translation machinery.

**Gene Regulation** — transcriptional control, regulatory networks, and gene expression dynamics:

#### Key Model Categories

**Transcription Factor & Signaling Networks:**
- NF-κB signaling and transcription models (Hoffmann, Ashall)
- p53 response systems (Hat, Purvis)
- IRF7 circuit and interferon response (Aguilera)
- STAT signaling and gene activation

**Gene Regulatory Networks:**
- Arabidopsis flower development GRNs (Azpeitia)
- Sea urchin embryonic GRNs (Flocand)
- Phage lambda lysogeny switch (Cao)
- Bacterial regulatory networks

**Post-Transcriptional Regulation:**
- mRNA translation machinery (Firczuk)
- miRNA sponge-mediated regulation (Dhawan)
- Translational control dynamics

**Epigenetic & Chromatin Regulation:**
- Epigenetic state maintenance
- Chromatin-mediated silencing models

**Disease-Related Gene Regulation:**
- Duchenne muscular dystrophy gene regulation (Grunwald)
- Cancer-related transcriptional programs

**Note:** This repository contains 43 models spanning transcriptional networks, post-transcriptional control, and epigenetic regulation. For a complete list, see the `models/` directory.

## Layout

```
models-generegulation/
├── models/<model-slug>/     # One model package per folder, each with model.yaml
├── libs/                    # Shared helper code for curated models
├── templates/model-pack/    # Starter template for new model packs
├── scripts/                 # Manifest and entrypoint validation scripts
├── docs/                    # Governance documentation
└── .github/workflows/       # CI/CD pipeline
```

## How It Works

### Model Interface

Every model implements the `biosim.BioModule` interface:

- **`inputs()`** — declares named input signals the module consumes
- **`outputs()`** — declares named output signals the module produces
- **`advance_to(t)`** — advances the model's internal state to time `t`

Most models include Python source under `src/` and can be wired together via `space.yaml` for multi-layered gene regulation studies.

### Model Standards

All models in this repository:
- Use SBML (Systems Biology Markup Language) format
- Are sourced from BioModels and curated regulatory network databases
- Include tellurium runtime for SBML execution
- Provide `state` output for monitoring gene expression dynamics
- Support configurable timesteps via `min_dt` parameter

## Getting Started

### Prerequisites

- Python 3.11+
- `biosim` framework

### Install biosim

```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

### Create a New Model

1. Copy `templates/model-pack/` to `models/<your-model-slug>/`
2. Edit `model.yaml` with metadata, entrypoint, and pinned dependencies
3. Implement your module (subclass `biosim.BioModule`)
4. Add gene regulation-specific tags
5. Validate: `python scripts/validate_manifests.py && python scripts/check_entrypoints.py`

## Linking in biosim-platform

- Models can be linked with explicit paths:
  - `models/generegulation-sbml-hoffmann2002-knockout-ikbnfkb-signaling/model.yaml`
- Gene regulation models can be composed with signaling, metabolism, or development models for multi-scale simulations

## Validation & CI

Three scripts enforce repository integrity on every push:

| Script | Purpose |
|--------|---------|
| `scripts/validate_manifests.py` | Schema validation for all model.yaml files |
| `scripts/check_entrypoints.py` | Verifies Python entrypoints are importable and callable |
| `scripts/check_public_boundary.sh` | Prevents business-sensitive content in this public repo |

The CI pipeline (`.github/workflows/ci.yml`) runs: **secret scan** → **manifest validation** → **smoke sandbox** (Docker).

## Contributing

- All dependencies must use exact version pinning (`==`)
- Model slugs use kebab-case with domain prefix (`generegulation-sbml-`)
- Models must follow the `biosim.BioModule` interface
- SBML models use tellurium runtime for execution
- Pre-commit hooks enforce trailing whitespace, EOF newlines, YAML syntax, and secret detection

## Domain-Specific Notes

**Gene Regulation Focus Areas:**
- **Transcription Factors**: NF-κB, p53, IRF7, STAT, and other key regulators
- **Gene Regulatory Networks**: Developmental programs, cell fate decisions, pattern formation
- **Signal-to-Transcription**: Coupling of signaling pathways to gene expression
- **Post-Transcriptional Control**: mRNA translation, miRNA regulation, RNA-binding proteins
- **Epigenetic Regulation**: Chromatin states, histone modifications, DNA methylation
- **Feedback Loops**: Autoregulation, mutual inhibition, toggle switches
- **Oscillatory Dynamics**: p53 pulses, NF-κB oscillations, circadian regulation

**Model Types:**
- ODE models of transcription factor networks
- Boolean/logical models of regulatory circuits
- Stochastic gene expression models
- Multi-scale models from signaling to transcription

## License

This repository is dual-licensed:

- **Code** (scripts, templates, Python modules): Apache-2.0 (`LICENSE-CODE.txt`)
- **Model/content** (manifests, docs, wiring/config): CC BY 4.0 (`LICENSE-CONTENT.txt`)

Attribution guidance: `ATTRIBUTION.md`
