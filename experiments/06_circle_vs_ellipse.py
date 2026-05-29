from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/06_circle_vs_ellipse.csv"
LOG_OUT = ROOT / "results/logs/06_circle_vs_ellipse.txt"

FIG_SHAPES = ROOT / "figures/06_circle_vs_ellipse_shapes.png"
FIG_FOCUS = ROOT / "figures/06_focus_separation.png"


# ------------------------------------------------------------
# Circle / Ellipse transition
# ------------------------------------------------------------
# Perfect coupling:
#   a = b
#   eccentricity = 0
#   focal separation = 0
#
# Partial coupling:
#   a > b
#   eccentricity > 0
#   focal separation > 0
#
# We map coupling coherence from Experiment 05 into ellipse deformation.
# coherence = 1 means circle.
# coherence < 1 means ellipse.
# ------------------------------------------------------------


coherence_values = np.array([
    1.00,
    0.97,
    0.88,
    0.75,
    0.58,
    0.25,
])

a = np.ones_like(coherence_values)
b = coherence_values

eccentricity = np.sqrt(1.0 - (b**2 / a**2))
focus_c = np.sqrt(a**2 - b**2)
focus_separation = 2.0 * focus_c

area = np.pi * a * b
circle_area = np.pi
area_ratio = area / circle_area

df = pd.DataFrame({
    "coherence": coherence_values,
    "a_major": a,
    "b_minor": b,
    "eccentricity": eccentricity,
    "focus_c": focus_c,
    "focus_separation": focus_separation,
    "area": area,
    "area_ratio_vs_circle": area_ratio,
})

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


# ------------------------------------------------------------
# Plot 1 — Shapes
# ------------------------------------------------------------

FIG_SHAPES.parent.mkdir(parents=True, exist_ok=True)

t = np.linspace(0, 2 * np.pi, 600)

plt.figure(figsize=(8, 8))

for coh in coherence_values:
    x = np.cos(t)
    y = coh * np.sin(t)
    plt.plot(x, y, label=f"coherence={coh:.2f}")

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.gca().set_aspect("equal", adjustable="box")

plt.title("Experiment 06 — Circle to Ellipse Transition")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.tight_layout()

plt.savefig(FIG_SHAPES)
plt.close()


# ------------------------------------------------------------
# Plot 2 — Focus separation
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(df["coherence"], df["focus_separation"], marker="o")
plt.gca().invert_xaxis()

plt.title("Experiment 06 — Focus Separation vs Coupling Coherence")
plt.xlabel("coupling coherence")
plt.ylabel("focus separation")

plt.tight_layout()
plt.savefig(FIG_FOCUS)
plt.close()


# ------------------------------------------------------------
# Log
# ------------------------------------------------------------

with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 06 — Circle vs Ellipse Transition\n\n")

    f.write("Mapping:\n")
    f.write("coherence = 1.0  -> circle\n")
    f.write("coherence < 1.0  -> ellipse\n\n")

    f.write("Rows:\n")
    for _, r in df.iterrows():
        f.write(
            f"coherence={r['coherence']:.6f} | "
            f"a={r['a_major']:.6f} | "
            f"b={r['b_minor']:.6f} | "
            f"eccentricity={r['eccentricity']:.6f} | "
            f"focus_separation={r['focus_separation']:.6f} | "
            f"area_ratio={r['area_ratio_vs_circle']:.6f}\n"
        )

    f.write("\nInterpretation:\n")
    f.write(
        "Perfect coupling is represented by a circle: the two foci collapse into one. "
        "When coupling coherence decreases, the circle becomes an ellipse and the "
        "focal structure separates. This provides the minimal geometric bridge "
        "from isotropic coupling to bifocal partial coupling.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 06 — Circle vs Ellipse Transition")
print()
print("coherence -> focus separation")
for _, r in df.iterrows():
    print(
        f"{r['coherence']:.6f} -> "
        f"ecc={r['eccentricity']:.6f}, "
        f"focus_sep={r['focus_separation']:.6f}, "
        f"area_ratio={r['area_ratio_vs_circle']:.6f}"
    )

print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_SHAPES)
print("FIG :", FIG_FOCUS)
