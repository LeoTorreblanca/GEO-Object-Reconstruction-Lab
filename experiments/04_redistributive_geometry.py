from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/04_redistributive_geometry.csv"
LOG_OUT = ROOT / "results/logs/04_redistributive_geometry.txt"

FIG_GAP = ROOT / "figures/04_redistributive_gap.png"
FIG_SYMMETRY = ROOT / "figures/04_redistributive_symmetry.png"


# ------------------------------------------------------------
# Redistributive geometry
# ------------------------------------------------------------
# Foundational rule:
#
# A(theta) + B(theta) = 1
#
# A: observable / active component
# B: complementary / redistributed component
#
# The gap is modeled as:
#
# G(theta) = A(theta) * B(theta)
#
# This is equivalent to:
#
# G(theta) = A(theta) - A(theta)^2
#
# when B = 1 - A.
#
# This experiment reconstructs the redistributive law before
# introducing circle/ellipse, tangent shadow, or object naming.
# ------------------------------------------------------------


theta = np.linspace(0.0, np.pi / 2.0, 2001)
theta_deg = np.degrees(theta)

A = np.cos(theta) ** 2
B = np.sin(theta) ** 2

G = A * B

conservation = A + B
conservation_error = np.max(np.abs(conservation - 1.0))

idx_max = int(np.argmax(G))

theta_max = theta[idx_max]
theta_max_deg = theta_deg[idx_max]

A_max = A[idx_max]
B_max = B[idx_max]
G_max = G[idx_max]

# Symmetric pairs around pi/4
theta_left = theta[theta <= np.pi / 4]
theta_right = (np.pi / 2) - theta_left

symmetry_pairs = pd.DataFrame(
    {
        "theta_left_deg": np.degrees(theta_left),
        "theta_right_deg": np.degrees(theta_right),
        "theta_sum_deg": np.degrees(theta_left + theta_right),
        "A_left": np.cos(theta_left) ** 2,
        "B_left": np.sin(theta_left) ** 2,
        "A_right": np.cos(theta_right) ** 2,
        "B_right": np.sin(theta_right) ** 2,
    }
)

symmetry_pairs["A_left_minus_B_right"] = (
    symmetry_pairs["A_left"] - symmetry_pairs["B_right"]
)

symmetry_pairs["B_left_minus_A_right"] = (
    symmetry_pairs["B_left"] - symmetry_pairs["A_right"]
)

symmetry_error = max(
    symmetry_pairs["A_left_minus_B_right"].abs().max(),
    symmetry_pairs["B_left_minus_A_right"].abs().max(),
)

df = pd.DataFrame(
    {
        "theta_rad": theta,
        "theta_deg": theta_deg,
        "A_observable": A,
        "B_complement": B,
        "A_plus_B": conservation,
        "G_gap": G,
    }
)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


# ------------------------------------------------------------
# Plot 1 — Gap
# ------------------------------------------------------------

FIG_GAP.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(9, 5))

plt.plot(theta_deg, G)
plt.axvline(theta_max_deg, linestyle="--")
plt.scatter([theta_max_deg], [G_max])

plt.title("Experiment 04 — Redistributive Gap")
plt.xlabel("theta (degrees)")
plt.ylabel("G = A·B")

plt.tight_layout()
plt.savefig(FIG_GAP)
plt.close()


# ------------------------------------------------------------
# Plot 2 — Symmetry
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

plt.plot(theta_deg, A, label="A observable")
plt.plot(theta_deg, B, label="B complement")
plt.plot(theta_deg, conservation, label="A + B")

plt.axvline(theta_max_deg, linestyle="--")

plt.title("Experiment 04 — Redistributive Symmetry")
plt.xlabel("theta (degrees)")
plt.ylabel("component value")

plt.legend()
plt.tight_layout()
plt.savefig(FIG_SYMMETRY)
plt.close()


# ------------------------------------------------------------
# Log
# ------------------------------------------------------------

with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 04 — Redistributive Geometry\n\n")

    f.write("Foundational law:\n")
    f.write("A(theta) + B(theta) = 1\n\n")

    f.write("Gap model:\n")
    f.write("G(theta) = A(theta) * B(theta)\n")
    f.write("G(theta) = A(theta) - A(theta)^2, when B = 1 - A\n\n")

    f.write("Maximum redistributive gap:\n")
    f.write(f"theta_max_rad       = {theta_max:.12f}\n")
    f.write(f"theta_max_deg       = {theta_max_deg:.12f}\n")
    f.write(f"A_at_max            = {A_max:.12f}\n")
    f.write(f"B_at_max            = {B_max:.12f}\n")
    f.write(f"G_max               = {G_max:.12f}\n\n")

    f.write("Conservation:\n")
    f.write(f"conservation_error  = {conservation_error:.18e}\n\n")

    f.write("Angular symmetry:\n")
    f.write("theta_left + theta_right = 90 degrees\n")
    f.write(f"symmetry_error      = {symmetry_error:.18e}\n\n")

    f.write("Interpretation:\n")
    f.write(
        "Starting only from A+B=1, the system produces a redistributive gap "
        "with maximum at the isotropic axis theta=pi/4. This reconstructs the "
        "first preformal GEO mathematical seed: conservation, redistribution, "
        "and angular symmetry appear before any physical object is named.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 04 — Redistributive Geometry")
print()
print("Foundational law:")
print("A(theta) + B(theta) = 1")
print()
print("Gap model:")
print("G(theta) = A(theta) * B(theta)")
print("G(theta) = A(theta) - A(theta)^2")
print()
print(f"theta_max_rad       = {theta_max:.12f}")
print(f"theta_max_deg       = {theta_max_deg:.12f}")
print(f"A_at_max            = {A_max:.12f}")
print(f"B_at_max            = {B_max:.12f}")
print(f"G_max               = {G_max:.12f}")
print(f"conservation_error  = {conservation_error:.18e}")
print(f"symmetry_error      = {symmetry_error:.18e}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_GAP)
print("FIG :", FIG_SYMMETRY)
