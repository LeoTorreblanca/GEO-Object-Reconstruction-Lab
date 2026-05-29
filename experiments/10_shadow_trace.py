from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/10_shadow_trace.csv"
LOG_OUT = ROOT / "results/logs/10_shadow_trace.txt"

FIG_TRACE = ROOT / "figures/10_shadow_trace.png"
FIG_BALANCE = ROOT / "figures/10_trace_balance.png"


# ------------------------------------------------------------
# Shadow trace reconstruction
# ------------------------------------------------------------
# Previous step:
#   phi = 90 - theta
#
# Here we construct two trace components:
#
#   S_normal  = sin(theta) * cos(phi)
#   S_tangent = cos(theta) * sin(phi)
#
# Since phi = 90 - theta, both traces meet near the isotropic
# balance axis. This is a minimal reconstruction of the trace
# before introducing tangent-plane terminology.
# ------------------------------------------------------------


theta_deg = np.linspace(10.0, 80.0, 1401)
theta = np.radians(theta_deg)

phi_deg = 90.0 - theta_deg
phi = np.radians(phi_deg)

S_normal = np.sin(theta) * np.cos(phi)
S_tangent = np.cos(theta) * np.sin(phi)

trace_sum = S_normal + S_tangent
trace_diff = np.abs(S_normal - S_tangent)

idx_balance = int(np.argmin(trace_diff))

theta_balance = theta_deg[idx_balance]
phi_balance = phi_deg[idx_balance]

S_normal_balance = S_normal[idx_balance]
S_tangent_balance = S_tangent[idx_balance]
trace_diff_balance = trace_diff[idx_balance]

df = pd.DataFrame({
    "theta_deg": theta_deg,
    "phi_deg": phi_deg,
    "S_normal": S_normal,
    "S_tangent": S_tangent,
    "trace_sum": trace_sum,
    "trace_diff": trace_diff,
})

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


FIG_TRACE.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(9, 5))
plt.plot(theta_deg, S_normal, label="S_normal")
plt.plot(theta_deg, S_tangent, label="S_tangent")
plt.axvline(theta_balance, linestyle="--")
plt.title("Experiment 10 — Shadow Trace Components")
plt.xlabel("theta (degrees)")
plt.ylabel("trace magnitude")
plt.legend()
plt.tight_layout()
plt.savefig(FIG_TRACE)
plt.close()


plt.figure(figsize=(9, 5))
plt.plot(theta_deg, trace_diff)
plt.axvline(theta_balance, linestyle="--")
plt.title("Experiment 10 — Trace Balance")
plt.xlabel("theta (degrees)")
plt.ylabel("|S_normal - S_tangent|")
plt.tight_layout()
plt.savefig(FIG_BALANCE)
plt.close()


with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 10 — Shadow Trace\n\n")

    f.write("Definitions:\n")
    f.write("phi = 90 - theta\n")
    f.write("S_normal  = sin(theta) * cos(phi)\n")
    f.write("S_tangent = cos(theta) * sin(phi)\n\n")

    f.write("Balance point:\n")
    f.write(f"theta_balance       = {theta_balance:.12f}\n")
    f.write(f"phi_balance         = {phi_balance:.12f}\n")
    f.write(f"S_normal_balance    = {S_normal_balance:.12f}\n")
    f.write(f"S_tangent_balance   = {S_tangent_balance:.12f}\n")
    f.write(f"trace_diff_balance  = {trace_diff_balance:.18e}\n\n")

    f.write("Interpretation:\n")
    f.write(
        "Using the orthogonal signature phi=90-theta, two trace components "
        "are reconstructed. Their balance occurs at the isotropic axis. "
        "This creates the first minimal trace model before naming a tangent plane "
        "or assigning physical meaning to the residual.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 10 — Shadow Trace")
print()
print(f"theta_balance       = {theta_balance:.12f}")
print(f"phi_balance         = {phi_balance:.12f}")
print(f"S_normal_balance    = {S_normal_balance:.12f}")
print(f"S_tangent_balance   = {S_tangent_balance:.12f}")
print(f"trace_diff_balance  = {trace_diff_balance:.18e}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_TRACE)
print("FIG :", FIG_BALANCE)
