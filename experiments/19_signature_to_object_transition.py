from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/19_signature_to_object_transition.csv"
LOG_OUT = ROOT / "results/logs/19_signature_to_object_transition.txt"
FIG_OUT = ROOT / "figures/19_signature_band.png"


s1 = 3 / 4
s2 = math.sqrt(3 / 5)
s3 = math.pi / 4

d12 = s2 - s1
d23 = s3 - s2
band_width = s3 - s1

center = (s1 + s3) / 2
offset_fc = s2 - center

rows = [
    {"signature": "3/4", "value": s1},
    {"signature": "sqrt(3/5)", "value": s2},
    {"signature": "pi/4", "value": s3},
]

df = pd.DataFrame(rows)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)

plt.figure(figsize=(8, 2))
plt.scatter(df["value"], [1, 1, 1], s=100)

for _, r in df.iterrows():
    plt.text(r["value"], 1.02, r["signature"])

plt.yticks([])
plt.xlabel("value")
plt.title("Experiment 19 — Signature Band")
plt.tight_layout()

FIG_OUT.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(FIG_OUT)
plt.close()


with open(LOG_OUT, "w") as f:

    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 19 — Signature to Object Transition\n\n")

    f.write("Observed signatures:\n\n")
    f.write(f"3/4         = {s1:.12f}\n")
    f.write(f"sqrt(3/5)   = {s2:.12f}\n")
    f.write(f"pi/4        = {s3:.12f}\n\n")

    f.write("Band structure:\n")
    f.write(f"d(3/4,fc)   = {d12:.12f}\n")
    f.write(f"d(fc,pi/4)  = {d23:.12f}\n")
    f.write(f"band_width  = {band_width:.12f}\n")
    f.write(f"band_center = {center:.12f}\n")
    f.write(f"fc_offset   = {offset_fc:.12e}\n\n")

    f.write("Interpretation:\n")
    f.write(
        "The three recurrent signatures form a compact invariant band. "
        "Before any operator is introduced, the laboratory observes a "
        "preferred geometric region bounded by 3/4 and pi/4, with "
        "sqrt(3/5) naturally embedded inside the band. This reconstructs "
        "the historical transition from repeated numerical signatures "
        "to geometric object identification.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 19 — Signature to Object Transition")
print()
print(f"3/4         = {s1:.12f}")
print(f"sqrt(3/5)   = {s2:.12f}")
print(f"pi/4        = {s3:.12f}")
print()
print(f"d(3/4,fc)   = {d12:.12f}")
print(f"d(fc,pi/4)  = {d23:.12f}")
print(f"band_width  = {band_width:.12f}")
print(f"fc_offset   = {offset_fc:.12e}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_OUT)
