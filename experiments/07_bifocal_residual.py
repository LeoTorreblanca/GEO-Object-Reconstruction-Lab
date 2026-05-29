from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/07_bifocal_residual.csv"
LOG_OUT = ROOT / "results/logs/07_bifocal_residual.txt"

FIG_FOCI = ROOT / "figures/07_bifocal_structure.png"
FIG_RESIDUAL = ROOT / "figures/07_residual_growth.png"


# ------------------------------------------------------------
# Bifocal reconstruction
# ------------------------------------------------------------

coherence_values = np.linspace(1.0, 0.25, 16)

a = np.ones_like(coherence_values)
b = coherence_values

focus_c = np.sqrt(a**2 - b**2)

left_focus = -focus_c
right_focus = focus_c

focus_separation = 2.0 * focus_c

# residual candidate

residual = 1.0 - coherence_values

df = pd.DataFrame({
    "coherence": coherence_values,
    "left_focus": left_focus,
    "right_focus": right_focus,
    "focus_separation": focus_separation,
    "residual": residual,
})

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


# ------------------------------------------------------------
# Plot 1
# ------------------------------------------------------------

FIG_FOCI.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(10, 5))

for _, row in df.iloc[::3].iterrows():

    plt.scatter(
        [row["left_focus"], row["right_focus"]],
        [row["coherence"], row["coherence"]]
    )

plt.title("Experiment 07 — Bifocal Structure")
plt.xlabel("focus position")
plt.ylabel("coherence")

plt.tight_layout()
plt.savefig(FIG_FOCI)
plt.close()


# ------------------------------------------------------------
# Plot 2
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(
    coherence_values,
    residual,
    marker="o"
)

plt.gca().invert_xaxis()

plt.title("Experiment 07 — Residual Emergence")
plt.xlabel("coherence")
plt.ylabel("residual")

plt.tight_layout()
plt.savefig(FIG_RESIDUAL)
plt.close()


# ------------------------------------------------------------
# Log
# ------------------------------------------------------------

with open(LOG_OUT, "w") as f:

    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 07 — Bifocal Residual\n\n")

    f.write(
        "Interpretation:\n"
        "As coherence decreases, a single focus separates into a bifocal "
        "structure. The residual grows together with focal separation.\n\n"
    )

    for _, row in df.iterrows():

        f.write(
            f"coherence={row['coherence']:.6f} | "
            f"left={row['left_focus']:.6f} | "
            f"right={row['right_focus']:.6f} | "
            f"sep={row['focus_separation']:.6f} | "
            f"residual={row['residual']:.6f}\n"
        )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 07 — Bifocal Residual")
print()

print(
    f"min coherence = {coherence_values.min():.6f}"
)
print(
    f"max focus separation = {focus_separation.max():.6f}"
)

print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_FOCI)
print("FIG :", FIG_RESIDUAL)
