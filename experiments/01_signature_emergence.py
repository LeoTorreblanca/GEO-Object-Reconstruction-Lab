from pathlib import Path
import pandas as pd

from core.geometric_invariants import INVARIANTS


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results" / "csv" / "01_signature_emergence.csv"
LOG_OUT = ROOT / "results" / "logs" / "01_signature_emergence.txt"


df = pd.DataFrame(
    [
        {
            "parameter": k,
            "value": v
        }
        for k, v in INVARIANTS.items()
    ]
)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(CSV_OUT, index=False)

with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 01 — Signature Emergence\n\n")

    for k, v in INVARIANTS.items():
        f.write(f"{k} = {v:.12f}\n")

print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
