from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/05_coupling_breakdown.csv"
LOG_OUT = ROOT / "results/logs/05_coupling_breakdown.txt"

FIG_LOSS = ROOT / "figures/05_coupling_loss.png"
FIG_IMBALANCE = ROOT / "figures/05_coupling_imbalance.png"


theta0 = np.pi / 4.0

theta = np.linspace(0.0, np.pi / 2.0, 2001)
theta_deg = np.degrees(theta)

A = np.cos(theta) ** 2
B = np.sin(theta) ** 2
G = A * B

G_max = 0.25

delta_theta = theta - theta0
delta_theta_deg = np.degrees(delta_theta)

imbalance = np.abs(A - B)
gap_loss = G_max - G
coherence = G / G_max

idx_iso = int(np.argmin(np.abs(theta - theta0)))

df = pd.DataFrame({
    "theta_rad": theta,
    "theta_deg": theta_deg,
    "delta_theta_rad": delta_theta,
    "delta_theta_deg": delta_theta_deg,
    "A_observable": A,
    "B_complement": B,
    "imbalance_abs_A_minus_B": imbalance,
    "G_gap": G,
    "gap_loss": gap_loss,
    "coherence_ratio": coherence,
})

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


# Plot 1 — coherence loss

FIG_LOSS.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(9, 5))
plt.plot(delta_theta_deg, coherence)
plt.axvline(0.0, linestyle="--")
plt.title("Experiment 05 — Coupling Coherence Around pi/4")
plt.xlabel("delta theta from pi/4 (degrees)")
plt.ylabel("coherence = G / Gmax")
plt.tight_layout()
plt.savefig(FIG_LOSS)
plt.close()


# Plot 2 — imbalance

plt.figure(figsize=(9, 5))
plt.plot(delta_theta_deg, imbalance)
plt.axvline(0.0, linestyle="--")
plt.title("Experiment 05 — Observable/Complement Imbalance")
plt.xlabel("delta theta from pi/4 (degrees)")
plt.ylabel("|A - B|")
plt.tight_layout()
plt.savefig(FIG_IMBALANCE)
plt.close()


# Key samples

sample_degrees = [-30, -20, -10, -5, 0, 5, 10, 20, 30]
sample_rows = []

for d in sample_degrees:
    target = theta0 + np.radians(d)
    idx = int(np.argmin(np.abs(theta - target)))
    sample_rows.append({
        "delta_deg": d,
        "theta_deg": theta_deg[idx],
        "A": A[idx],
        "B": B[idx],
        "G": G[idx],
        "coherence": coherence[idx],
        "imbalance": imbalance[idx],
        "gap_loss": gap_loss[idx],
    })


with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 05 — Coupling Breakdown\n\n")

    f.write("Reference point:\n")
    f.write("theta0 = pi/4\n")
    f.write(f"theta0_deg = {np.degrees(theta0):.12f}\n\n")

    f.write("At isotropic coupling:\n")
    f.write(f"A = {A[idx_iso]:.12f}\n")
    f.write(f"B = {B[idx_iso]:.12f}\n")
    f.write(f"G = {G[idx_iso]:.12f}\n")
    f.write(f"coherence = {coherence[idx_iso]:.12f}\n")
    f.write(f"imbalance = {imbalance[idx_iso]:.12f}\n\n")

    f.write("Samples around pi/4:\n")
    for r in sample_rows:
        f.write(
            f"delta={r['delta_deg']:>4} deg | "
            f"theta={r['theta_deg']:.6f} | "
            f"A={r['A']:.6f} | "
            f"B={r['B']:.6f} | "
            f"G={r['G']:.6f} | "
            f"coherence={r['coherence']:.6f} | "
            f"imbalance={r['imbalance']:.6f} | "
            f"gap_loss={r['gap_loss']:.6f}\n"
        )

    f.write("\nInterpretation:\n")
    f.write(
        "The isotropic point pi/4 gives maximum coupling coherence. "
        "Moving away from pi/4 preserves A+B=1 but introduces imbalance, "
        "gap loss, and partial coupling. This prepares the geometric transition "
        "from perfect circular coupling to an anisotropic representation.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 05 — Coupling Breakdown")
print()
print(f"theta0_deg = {np.degrees(theta0):.12f}")
print(f"A_iso      = {A[idx_iso]:.12f}")
print(f"B_iso      = {B[idx_iso]:.12f}")
print(f"G_iso      = {G[idx_iso]:.12f}")
print(f"coherence  = {coherence[idx_iso]:.12f}")
print(f"imbalance  = {imbalance[idx_iso]:.12f}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_LOSS)
print("FIG :", FIG_IMBALANCE)
