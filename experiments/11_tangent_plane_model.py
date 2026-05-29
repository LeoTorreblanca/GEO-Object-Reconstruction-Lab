from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/11_tangent_plane_model.csv"
LOG_OUT = ROOT / "results/logs/11_tangent_plane_model.txt"

FIG_PLANE = ROOT / "figures/11_tangent_plane_model.png"
FIG_DISTANCE = ROOT / "figures/11_tangent_distance.png"


# ------------------------------------------------------------
# Tangent plane reconstruction
# ------------------------------------------------------------
# From Experiment 10:
#   S_normal  = sin(theta) * cos(phi)
#   S_tangent = cos(theta) * sin(phi)
#
# with:
#   phi = 90 - theta
#
# Here we reinterpret S_tangent as the coordinate of a
# tangent-plane trace. This is still geometric only.
# ------------------------------------------------------------


theta_deg = np.linspace(10.0, 80.0, 1401)
theta = np.radians(theta_deg)

phi_deg = 90.0 - theta_deg
phi = np.radians(phi_deg)

S_normal = np.sin(theta) * np.cos(phi)
S_tangent = np.cos(theta) * np.sin(phi)

# Tangent plane coordinates:
x_plane = theta_deg - 45.0
y_plane = S_tangent - S_normal

distance_from_balance = np.sqrt(x_plane**2 + y_plane**2)

idx_min = int(np.argmin(distance_from_balance))

theta_balance = theta_deg[idx_min]
phi_balance = phi_deg[idx_min]
x_balance = x_plane[idx_min]
y_balance = y_plane[idx_min]
distance_balance = distance_from_balance[idx_min]

df = pd.DataFrame({
    "theta_deg": theta_deg,
    "phi_deg": phi_deg,
    "S_normal": S_normal,
    "S_tangent": S_tangent,
    "x_plane": x_plane,
    "y_plane": y_plane,
    "distance_from_balance": distance_from_balance,
})

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


FIG_PLANE.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 6))
plt.plot(x_plane, y_plane)
plt.scatter([x_balance], [y_balance])
plt.axhline(0.0, linestyle="--")
plt.axvline(0.0, linestyle="--")
plt.title("Experiment 11 — Tangent Plane Trace")
plt.xlabel("theta - 45°")
plt.ylabel("S_tangent - S_normal")
plt.tight_layout()
plt.savefig(FIG_PLANE)
plt.close()


plt.figure(figsize=(9, 5))
plt.plot(theta_deg, distance_from_balance)
plt.axvline(theta_balance, linestyle="--")
plt.title("Experiment 11 — Distance from Tangent Balance")
plt.xlabel("theta (degrees)")
plt.ylabel("distance from balance")
plt.tight_layout()
plt.savefig(FIG_DISTANCE)
plt.close()


with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 11 — Tangent Plane Model\n\n")

    f.write("Definitions:\n")
    f.write("x_plane = theta - 45 degrees\n")
    f.write("y_plane = S_tangent - S_normal\n\n")

    f.write("Balance point:\n")
    f.write(f"theta_balance        = {theta_balance:.12f}\n")
    f.write(f"phi_balance          = {phi_balance:.12f}\n")
    f.write(f"x_balance            = {x_balance:.12f}\n")
    f.write(f"y_balance            = {y_balance:.12f}\n")
    f.write(f"distance_balance     = {distance_balance:.18e}\n\n")

    f.write("Interpretation:\n")
    f.write(
        "The orthogonal trace can be represented as a tangent-plane coordinate "
        "system centered at the isotropic axis. At theta=45 degrees, normal and "
        "tangent components balance and the tangent-plane trace crosses the origin. "
        "This reconstructs the tangent plane as a geometric consequence of "
        "orthogonal projection, not as an independent assumption.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 11 — Tangent Plane Model")
print()
print(f"theta_balance        = {theta_balance:.12f}")
print(f"phi_balance          = {phi_balance:.12f}")
print(f"x_balance            = {x_balance:.12f}")
print(f"y_balance            = {y_balance:.12f}")
print(f"distance_balance     = {distance_balance:.18e}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_PLANE)
print("FIG :", FIG_DISTANCE)
