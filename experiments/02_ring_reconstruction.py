from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from core.geometric_invariants import (
    ETA,
    FC,
    THREE_QUARTERS,
    PI_OVER_FOUR
)

ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/02_ring_reconstruction.csv"
LOG_OUT = ROOT / "results/logs/02_ring_reconstruction.txt"

FIG_RING = ROOT / "figures/02_ring_band.png"
FIG_DISTANCE = ROOT / "figures/02_ring_distance.png"


# ----------------------------------
# Geometric signatures
# ----------------------------------

values = {
    "three_quarters": THREE_QUARTERS,
    "fc": FC,
    "pi_over_four": PI_OVER_FOUR,
}

ring_min = min(values.values())
ring_max = max(values.values())

ring_center = np.mean(list(values.values()))

ring_width = ring_max - ring_min


# ----------------------------------
# Dataframe
# ----------------------------------

df = pd.DataFrame(
    [
        {
            "signature": k,
            "value": v,
            "distance_to_center": abs(v - ring_center)
        }
        for k, v in values.items()
    ]
)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(CSV_OUT, index=False)


# ----------------------------------
# Plot 1
# ----------------------------------

plt.figure(figsize=(8, 4))

plt.axvline(ring_min, linestyle="--")
plt.axvline(ring_max, linestyle="--")

plt.scatter(
    list(values.values()),
    [1, 1, 1]
)

for k, v in values.items():
    plt.text(v, 1.01, k)

plt.title("GEO Ring Reconstruction")
plt.yticks([])

plt.tight_layout()

FIG_RING.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(FIG_RING)
plt.close()


# ----------------------------------
# Plot 2
# ----------------------------------

plt.figure(figsize=(8, 4))

plt.bar(
    df["signature"],
    df["distance_to_center"]
)

plt.title("Distance to Ring Center")

plt.tight_layout()

plt.savefig(FIG_DISTANCE)
plt.close()


# ----------------------------------
# Log
# ----------------------------------

with open(LOG_OUT, "w") as f:

    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 02 — Ring Reconstruction\n\n")

    f.write(f"ring_min    = {ring_min:.12f}\n")
    f.write(f"ring_max    = {ring_max:.12f}\n")
    f.write(f"ring_center = {ring_center:.12f}\n")
    f.write(f"ring_width  = {ring_width:.12f}\n\n")

    f.write("Signatures\n")

    for k, v in values.items():
        f.write(f"{k:20s} {v:.12f}\n")


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 02 — Ring Reconstruction")

print()
print(f"ring_min    = {ring_min:.12f}")
print(f"ring_max    = {ring_max:.12f}")
print(f"ring_center = {ring_center:.12f}")
print(f"ring_width  = {ring_width:.12f}")

print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_RING)
print("FIG :", FIG_DISTANCE)
