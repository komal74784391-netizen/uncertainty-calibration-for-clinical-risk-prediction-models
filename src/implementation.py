"""Calibration utilities for clinical risk prediction models."""

from dataclasses import dataclass

import numpy as np


@dataclass
class CalibrationResult:
    expected_calibration_error: float
    brier_score: float
    reliability_bins: list[tuple[float, float, int]]


def reliability_curve(probabilities: np.ndarray, labels: np.ndarray, bins: int = 10):
    edges = np.linspace(0.0, 1.0, bins + 1)
    out = []
    for low, high in zip(edges[:-1], edges[1:]):
        members = (probabilities >= low) & (probabilities < high)
        if members.any():
            out.append((float(probabilities[members].mean()), float(labels[members].mean()), int(members.sum())))
    return out


def evaluate_calibration(probabilities, labels, bins: int = 10) -> CalibrationResult:
    probabilities = np.asarray(probabilities, dtype=float)
    labels = np.asarray(labels, dtype=float)
    curve = reliability_curve(probabilities, labels, bins)
    total = max(len(probabilities), 1)
    ece = sum(abs(conf - acc) * count / total for conf, acc, count in curve)
    brier = float(np.mean((probabilities - labels) ** 2))
    return CalibrationResult(float(ece), brier, curve)
