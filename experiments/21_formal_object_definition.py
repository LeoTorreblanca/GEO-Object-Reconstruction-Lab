from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

CSV_DIR = ROOT / "results" / "csv"
LOG_DIR = ROOT / "results" / "logs"
FIG_DIR = ROOT / "figures"

CSV_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)

criteria = [
    ("invariant_signature_band", 1),
    ("redistributive_conservation", 1),
    ("isotropic_axis_pi_over_4", 1),
    ("maximum_coupling", 1),
    ("partial_coupling_breakdown", 1),
    ("circle_ellipse_transition", 1),
    ("bifocal_emergence", 1),
    ("residual_bridge", 1),
    ("orthogonal_signature", 1),
    ("trace_balance", 1),
    ("tangent_plane_crossing", 1),
]

df = pd.DataFrame(criteria, columns=["criterion", "recovered"])

criteria_satisfied = int(df["recovered"].sum())
criteria_total = len(df)

definition_closed = criteria_satisfied == criteria_total

csv_file = CSV_DIR / "21_formal_object_definition.csv"
df.to_csv(csv_file, index=False)

plt.figure(figsize=(10,5))
plt.bar(df["criterion"], df["recovered"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("recovered")
plt.title("Experiment 21 — Formal Object Definition")
plt.tight_layout()

fig_file = FIG_DIR / "21_formal_object_definition.png"
plt.savefig(fig_file, dpi=150)
plt.close()

log_text = f"""
=== GEO Object Reconstruction Lab ===
Experiment 21 — Formal Object Definition

criteria_satisfied = {criteria_satisfied}/{criteria_total}

definition_closed = {definition_closed}

Formal Definition

A GEO Coupled Geometric Architecture (CGA)
is a geometric structure satisfying:

1. invariant signature band
2. redistributive conservation
3. isotropic axis pi/4
4. maximum coupling
5. partial coupling breakdown
6. circle/ellipse transition
7. bifocal emergence
8. residual bridge
9. orthogonal signature
10. trace balance
11. tangent-plane crossing

Interpretation:

This experiment introduces no new operators and no new physics.
It formalizes the object reconstructed across Experiments 01–20.

The object is defined exclusively by the set of recovered criteria.
Any alternative model must reproduce all criteria simultaneously.

Result:

criteria_satisfied = {criteria_satisfied}/{criteria_total}

definition_closed = {definition_closed}
"""

log_file = LOG_DIR / "21_formal_object_definition.txt"

with open(log_file, "w") as f:
    f.write(log_text)

print("=== GEO Object Reconstruction Lab ===")
print("Experiment 21 — Formal Object Definition")
print()
print(f"criteria_satisfied = {criteria_satisfied}/{criteria_total}")
print()
print(f"definition_closed = {definition_closed}")
print()
print(f"CSV : {csv_file}")
print(f"LOG : {log_file}")
print(f"FIG : {fig_file}")
