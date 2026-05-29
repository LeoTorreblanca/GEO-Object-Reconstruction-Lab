from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/09_orthogonal_signature.csv"
LOG_OUT = ROOT / "results/logs/09_orthogonal_signature.txt"

FIG_SIGNATURE = ROOT / "figures/09_orthogonal_signature.png"


theta = np.linspace(0.0, 90.0, 1801)

phi = 90.0 - theta

difference = np.abs(theta - phi)

idx_eq = int(np.argmin(difference))

theta_eq = theta[idx_eq]
phi_eq = phi[idx_eq]

orthogonality_error = np.max(
    np.abs(theta + phi - 90.0)
)

df = pd.DataFrame({
    "theta_deg": theta,
    "phi_deg": phi,
    "theta_plus_phi": theta + phi,
    "difference": difference,
})

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


plt.figure(figsize=(9, 5))

plt.plot(theta, theta, label="theta")
plt.plot(theta, phi, label="90-theta")

plt.axvline(theta_eq, linestyle="--")

plt.title("Experiment 09 — Orthogonal Signature")
plt.xlabel("theta (degrees)")
plt.ylabel("orientation")

plt.legend()
plt.tight_layout()

FIG_SIGNATURE.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(FIG_SIGNATURE)
plt.close()


with open(LOG_OUT, "w") as f:

    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 09 — Orthogonal Signature\n\n")

    f.write(
        "Complementary orientation:\n"
        "phi = 90 - theta\n\n"
    )

    f.write(
        f"theta_eq = {theta_eq:.12f}\n"
    )

    f.write(
        f"phi_eq   = {phi_eq:.12f}\n"
    )

    f.write(
        f"orthogonality_error = "
        f"{orthogonality_error:.18e}\n\n"
    )

    f.write(
        "Interpretation:\n"
        "The complementary orientation remains orthogonal "
        "for all theta. Equality appears at 45 degrees, "
        "identifying the isotropic balance axis recovered "
        "through orientation rather than redistribution.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 09 — Orthogonal Signature")
print()
print(f"theta_eq = {theta_eq:.12f}")
print(f"phi_eq   = {phi_eq:.12f}")
print(
    f"orthogonality_error = "
    f"{orthogonality_error:.18e}"
)
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_SIGNATURE)
