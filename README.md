# uncertainty-calibration-for-clinical-risk-prediction-models

This repository contains the complete implementation of the paper
**Uncertainty Calibration for Clinical Risk Prediction Models**, accepted at Clinical Informatics Journal 2026.

## Components

- `src/` — reference implementation used to produce the published results
- `requirements.txt` — pinned dependencies
- `scripts/` — command line entry points

## Reproducing the results

```
pip install -r requirements.txt
python scripts/run_experiment.py --config configs/default.json
```

The released release tag `v1.0.0` corresponds to the camera-ready artefact.
