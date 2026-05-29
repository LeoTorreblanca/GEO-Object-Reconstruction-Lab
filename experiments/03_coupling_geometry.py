from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/03_coupling_geometry.csv"
LOG_OUT = ROOT / "results/logs/03_coupling_geometry.txt"

FIG_COUPLING = ROOT / "figures/03_coupling_gap.png"
FIG_COMPONENTS = ROOT / "figures/03_coupling_components.png"


# ----------------------------------
# Coupling model
# ----------------------------------
# A = observable component
# B = complementary component
# G = coupling/gap = A * B
#
# Here we use a pure angular decomposition:
# A(theta) = cos²(theta)
# B(theta) = sin²(theta)
# A + B = 1
# G(theta) = A * B

theta = np.linspace(0, np.pi / 2, 1001)

A = np.cos(theta) ** 2
B = np.sin(theta) ** 2
G = A * B

idx_max = int(np.argmax(G))

theta_max = theta[idx_max]
theta_max_deg = np.degrees(theta_max)

A_max = A[idx_max]
B_max = B[idx_max]
G_max = G[idx_max]

conservation_error = np.max(np.abs((A + B) - 1.0))


df = pd.DataFrame(
    {
        "theta_rad": theta,
        "theta_deg": np.degrees(theta),
        "A_observable": A,
        "B_complement": B,
        "G_coupling": G,
        "A_plus_B": A + B,
    }
)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


# ----------------------------------
# Plot 1 — coupling gap
# ----------------------------------

FIG_COUPLING.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
plt.plot(df["theta_deg"], df["G_coupling"])
plt.axvline(theta_max_deg, linestyle="--")
plt.title("Experiment 03 — Coupling Gap G = A·B")
plt.xlabel("theta (degrees)")
plt.ylabel("G")
plt.tight_layout()
plt.savefig(FIG_COUPLING)
plt.close()


# ----------------------------------
# Plot 2 — components
# ----------------------------------

plt.figure(figsize=(8, 5))
plt.plot(df["theta_deg"], df["A_observable"], label="A observable")
plt.plot(df["theta_deg"], df["B_complement"], label="B complement")
plt.axvline(theta_max_deg, linestyle="--")
plt.title("Experiment 03 — Observable / Complement Components")
plt.xlabel("theta (degrees)")
plt.ylabel("component")
plt.legend()
plt.tight_layout()
plt.savefig(FIG_COMPONENTS)
plt.close()


# ----------------------------------
# Log
# ----------------------------------

with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 03 — Coupling Geometry\n\n")

    f.write("Angular decomposition:\n")
    f.write("A(theta) = cos^2(theta)\n")
    f.write("B(theta) = sin^2(theta)\n")
    f.write("G(theta) = A(theta) * B(theta)\n\n")

    f.write(f"theta_max_rad       = {theta_max:.12f}\n")
    f.write(f"theta_max_deg       = {theta_max_deg:.12f}\n")
    f.write(f"A_at_max            = {A_max:.12f}\n")
    f.write(f"B_at_max            = {B_max:.12f}\n")
    f.write(f"G_max               = {G_max:.12f}\n")
    f.write(f"conservation_error  = {conservation_error:.18e}\n\n")

    f.write("Interpretation:\n")
    f.write(
        "The coupling gap reaches its maximum when observable and complementary "
        "components are balanced. This identifies the pi/4 axis as the natural "
        "isotropic coupling point of the minimal geometry.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 03 — Coupling Geometry")
print()
print(f"theta_max_rad       = {theta_max:.12f}")
print(f"theta_max_deg       = {theta_max_deg:.12f}")
print(f"A_at_max            = {A_max:.12f}")
print(f"B_at_max            = {B_max:.12f}")
print(f"G_max               = {G_max:.12f}")
print(f"conservation_error  = {conservation_error:.18e}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_COUPLING)
print("FIG :", FIG_COMPONENTS)
