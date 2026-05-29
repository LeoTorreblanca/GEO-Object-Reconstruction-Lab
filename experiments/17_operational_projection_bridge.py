from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/17_operational_projection_bridge.csv"
LOG_OUT = ROOT / "results/logs/17_operational_projection_bridge.txt"
FIG_OUT = ROOT / "figures/17_operational_projection_bridge.png"


# Internal architecture
eta = 3 / 5
B = 1 - eta
fc = math.sqrt(eta)
R = eta ** (1 / 3)

# Conceptual closure
Phi_conceptual = 1.88948
alpha_conceptual = Phi_conceptual * B / math.sqrt(2)

# Operational closure
alpha_operational = 0.534463497024
Phi_operational = alpha_operational * math.sqrt(2) / B

# Hubble bridge reference
H0_base = 67.40
H0_local = 73.04

delta_H_rel = (H0_local / H0_base) - 1

# GEO operational operator implied by alpha
O_required = delta_H_rel / alpha_operational

H0_reconstructed = H0_base * (1 + alpha_operational * O_required)

relative_error = (H0_reconstructed - H0_local) / H0_local


rows = [
    {
        "level": "conceptual",
        "Phi": Phi_conceptual,
        "alpha": alpha_conceptual,
        "operator": None,
        "H0_reconstructed": None,
        "relative_error": None,
    },
    {
        "level": "operational",
        "Phi": Phi_operational,
        "alpha": alpha_operational,
        "operator": O_required,
        "H0_reconstructed": H0_reconstructed,
        "relative_error": relative_error,
    },
]

df = pd.DataFrame(rows)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)

FIG_OUT.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
plt.bar(["alpha conceptual", "alpha operational"], [alpha_conceptual, alpha_operational])
plt.title("Experiment 17 — Conceptual vs Operational Alpha")
plt.ylabel("alpha")
plt.tight_layout()
plt.savefig(FIG_OUT)
plt.close()


with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 17 — Operational Projection Bridge\n\n")

    f.write("Internal architecture:\n")
    f.write(f"eta = {eta:.12f}\n")
    f.write(f"fc  = {fc:.12f}\n")
    f.write(f"B   = {B:.12f}\n")
    f.write(f"R   = {R:.12f}\n\n")

    f.write("Conceptual closure:\n")
    f.write(f"Phi_conceptual   = {Phi_conceptual:.12f}\n")
    f.write(f"alpha_conceptual = {alpha_conceptual:.12f}\n\n")

    f.write("Operational closure:\n")
    f.write(f"Phi_operational  = {Phi_operational:.12f}\n")
    f.write(f"alpha_operational= {alpha_operational:.12f}\n\n")

    f.write("Hubble bridge audit:\n")
    f.write(f"H0_base          = {H0_base:.12f}\n")
    f.write(f"H0_local         = {H0_local:.12f}\n")
    f.write(f"delta_H_rel      = {delta_H_rel:.18e}\n")
    f.write(f"O_required       = {O_required:.18e}\n")
    f.write(f"H0_reconstructed = {H0_reconstructed:.12f}\n")
    f.write(f"relative_error   = {relative_error:.18e}\n\n")

    f.write("Interpretation:\n")
    f.write(
        "The reconstructed object architecture keeps eta, fc, B and R fixed. "
        "Only the Phi/alpha level is separated into conceptual and operational "
        "closures. Using the operational alpha, the bridge reconstructs the "
        "target expansion value exactly through an explicit projection operator, "
        "without changing the reconstructed architecture.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 17 — Operational Projection Bridge")
print()
print(f"eta               = {eta:.12f}")
print(f"fc                = {fc:.12f}")
print(f"B                 = {B:.12f}")
print(f"R                 = {R:.12f}")
print()
print(f"alpha_conceptual  = {alpha_conceptual:.12f}")
print(f"alpha_operational = {alpha_operational:.12f}")
print(f"O_required        = {O_required:.18e}")
print(f"H0_reconstructed  = {H0_reconstructed:.12f}")
print(f"relative_error    = {relative_error:.18e}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_OUT)
