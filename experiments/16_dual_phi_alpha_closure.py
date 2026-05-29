from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/16_dual_phi_alpha_closure.csv"
LOG_OUT = ROOT / "results/logs/16_dual_phi_alpha_closure.txt"
FIG_OUT = ROOT / "figures/16_dual_phi_alpha_closure.png"


eta = 3 / 5
B = 1 - eta

phi_conceptual = 1.88948

alpha_conceptual = phi_conceptual * B / math.sqrt(2)

alpha_operational_target = 0.534463497024

phi_operational = alpha_operational_target * math.sqrt(2) / B

alpha_operational_check = phi_operational * B / math.sqrt(2)

phi_delta = phi_operational - phi_conceptual
alpha_delta = alpha_operational_target - alpha_conceptual

rows = [
    {
        "closure": "conceptual_internal",
        "Phi": phi_conceptual,
        "alpha": alpha_conceptual,
        "alpha_target": alpha_operational_target,
        "alpha_error": alpha_conceptual - alpha_operational_target,
        "interpretation": "internal framework conceptual ring depth"
    },
    {
        "closure": "operational_reconstructed",
        "Phi": phi_operational,
        "alpha": alpha_operational_check,
        "alpha_target": alpha_operational_target,
        "alpha_error": alpha_operational_check - alpha_operational_target,
        "interpretation": "Phi reconstructed from operational alpha target"
    },
]

df = pd.DataFrame(rows)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)

FIG_OUT.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
plt.bar(df["closure"], df["alpha_error"].abs())
plt.title("Experiment 16 — Alpha Closure Error")
plt.ylabel("|alpha error|")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(FIG_OUT)
plt.close()


with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 16 — Dual Phi/Alpha Closure\n\n")

    f.write("Shared operators:\n")
    f.write(f"eta = {eta:.12f}\n")
    f.write(f"B   = {B:.12f}\n\n")

    f.write("Conceptual internal closure:\n")
    f.write(f"Phi_conceptual      = {phi_conceptual:.12f}\n")
    f.write(f"alpha_conceptual    = {alpha_conceptual:.12f}\n\n")

    f.write("Operational reconstructed closure:\n")
    f.write(f"alpha_target        = {alpha_operational_target:.12f}\n")
    f.write(f"Phi_operational     = {phi_operational:.12f}\n")
    f.write(f"alpha_check         = {alpha_operational_check:.12f}\n\n")

    f.write("Deltas:\n")
    f.write(f"Phi_delta           = {phi_delta:.18e}\n")
    f.write(f"alpha_delta         = {alpha_delta:.18e}\n\n")

    f.write("Interpretation:\n")
    f.write(
        "The conceptual GEO framework value Phi=1.88948 and the operational "
        "Phi reconstructed from the alpha target are extremely close but not "
        "identical. This experiment keeps both closures separated: conceptual "
        "internal depth and operational reconstructed closure. This avoids "
        "conflating the framework approximation with the exact operational "
        "Hubble/Vacuum closure.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 16 — Dual Phi/Alpha Closure")
print()
print(f"Phi_conceptual   = {phi_conceptual:.12f}")
print(f"alpha_conceptual = {alpha_conceptual:.12f}")
print()
print(f"alpha_target     = {alpha_operational_target:.12f}")
print(f"Phi_operational  = {phi_operational:.12f}")
print(f"alpha_check      = {alpha_operational_check:.12f}")
print()
print(f"Phi_delta        = {phi_delta:.18e}")
print(f"alpha_delta      = {alpha_delta:.18e}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_OUT)
