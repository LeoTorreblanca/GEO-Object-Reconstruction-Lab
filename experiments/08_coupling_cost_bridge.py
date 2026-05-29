from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/08_coupling_cost_bridge.csv"
LOG_OUT = ROOT / "results/logs/08_coupling_cost_bridge.txt"

FIG_COST = ROOT / "figures/08_coupling_cost_bridge.png"
FIG_STORAGE = ROOT / "figures/08_between_focus_storage.png"


coherence = np.linspace(1.0, 0.25, 200)

a = np.ones_like(coherence)
b = coherence

focus_c = np.sqrt(a**2 - b**2)
focus_separation = 2.0 * focus_c

residual = 1.0 - coherence

# Coupling cost candidate:
# zero under perfect coupling,
# grows with both residual and focal separation.
coupling_cost = residual * focus_separation

# Normalized between-focus storage:
# interpreted as residual accumulated in the bridge between foci.
storage = coupling_cost / np.max(coupling_cost)

df = pd.DataFrame({
    "coherence": coherence,
    "b_minor": b,
    "focus_c": focus_c,
    "focus_separation": focus_separation,
    "residual": residual,
    "coupling_cost": coupling_cost,
    "between_focus_storage": storage,
})

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


FIG_COST.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(9, 5))
plt.plot(df["coherence"], df["coupling_cost"])
plt.gca().invert_xaxis()
plt.title("Experiment 08 — Coupling Cost Bridge")
plt.xlabel("coherence")
plt.ylabel("coupling cost = residual × focus separation")
plt.tight_layout()
plt.savefig(FIG_COST)
plt.close()


plt.figure(figsize=(9, 5))
plt.plot(df["focus_separation"], df["between_focus_storage"])
plt.title("Experiment 08 — Between-Focus Storage")
plt.xlabel("focus separation")
plt.ylabel("normalized storage")
plt.tight_layout()
plt.savefig(FIG_STORAGE)
plt.close()


# key points

sample_coherence = [1.00, 0.97, 0.88, 0.75, 0.60, 0.50, 0.25]
sample_rows = []

for c in sample_coherence:
    idx = int(np.argmin(np.abs(coherence - c)))
    sample_rows.append(df.iloc[idx].to_dict())


with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 08 — Coupling Cost Bridge\n\n")

    f.write("Definition:\n")
    f.write("coupling_cost = residual * focus_separation\n")
    f.write("residual = 1 - coherence\n\n")

    f.write("Key samples:\n")

    for r in sample_rows:
        f.write(
            f"coherence={r['coherence']:.6f} | "
            f"focus_sep={r['focus_separation']:.6f} | "
            f"residual={r['residual']:.6f} | "
            f"cost={r['coupling_cost']:.6f} | "
            f"storage={r['between_focus_storage']:.6f}\n"
        )

    f.write("\nInterpretation:\n")
    f.write(
        "The bifocal structure does not only separate into two points. "
        "As coherence decreases, a coupling cost appears between the foci. "
        "This cost is interpreted here as a geometric bridge variable: "
        "a precursor to tangent-plane residual storage, before introducing "
        "shadow terminology.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 08 — Coupling Cost Bridge")
print()
print("max_focus_separation =", float(np.max(focus_separation)))
print("max_coupling_cost    =", float(np.max(coupling_cost)))
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_COST)
print("FIG :", FIG_STORAGE)
