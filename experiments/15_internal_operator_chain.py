from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/15_internal_operator_chain.csv"
LOG_OUT = ROOT / "results/logs/15_internal_operator_chain.txt"
FIG_OUT = ROOT / "figures/15_internal_operator_chain.png"


eta = 3 / 5
fc = math.sqrt(eta)
B = 1 - eta

phi_internal = 1.88948
alpha = phi_internal * B / math.sqrt(2)

R = eta ** (1 / 3)

rows = [
    {
        "operator": "eta",
        "value": eta,
        "meaning": "natural active partition of the reconstructed object"
    },
    {
        "operator": "fc",
        "value": fc,
        "meaning": "causal operational boundary sqrt(eta)"
    },
    {
        "operator": "B",
        "value": B,
        "meaning": "free geometric sector 1-eta"
    },
    {
        "operator": "Phi",
        "value": phi_internal,
        "meaning": "coherent transfer depth of the internal ring"
    },
    {
        "operator": "alpha",
        "value": alpha,
        "meaning": "observable projection amplitude Phi*B/sqrt(2)"
    },
    {
        "operator": "R",
        "value": R,
        "meaning": "operational transfer scale eta^(1/3)"
    },
]

df = pd.DataFrame(rows)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)

FIG_OUT.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(9, 5))
plt.bar(df["operator"], df["value"])
plt.title("Experiment 15 — Internal GEO Operator Chain")
plt.ylabel("value")
plt.tight_layout()
plt.savefig(FIG_OUT)
plt.close()

with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 15 — Internal Operator Chain\n\n")

    f.write("Internal chain:\n")
    f.write("eta -> fc -> B -> Phi -> alpha -> R -> Observable\n\n")

    for _, r in df.iterrows():
        f.write(
            f"{r['operator']:8s} = {r['value']:.12f} | "
            f"{r['meaning']}\n"
        )

    f.write("\nClosure equations:\n")
    f.write("eta = 3/5\n")
    f.write("fc = sqrt(eta)\n")
    f.write("B = 1 - eta\n")
    f.write("alpha = Phi * B / sqrt(2)\n")
    f.write("R = eta^(1/3)\n\n")

    f.write("Interpretation:\n")
    f.write(
        "The reconstructed object is now connected to the mature internal GEO "
        "operator chain. eta describes the natural active partition, fc its "
        "causal boundary, B the free geometric sector, Phi the coherent internal "
        "depth, alpha the projected observable amplitude, and R the operational "
        "transfer scale.\n"
    )

print("=== GEO Object Reconstruction Lab ===")
print("Experiment 15 — Internal Operator Chain")
print()
for _, r in df.iterrows():
    print(f"{r['operator']:8s} = {r['value']:.12f}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_OUT)
