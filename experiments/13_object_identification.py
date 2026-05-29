from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/13_object_identification.csv"
LOG_OUT = ROOT / "results/logs/13_object_identification.txt"

FIG_OUT = ROOT / "figures/13_object_identification_score.png"


criteria = [
    {
        "criterion": "invariant_band",
        "description": "Original band containing 3/4, sqrt(3/5), pi/4",
        "status": 1,
        "evidence": "Experiment 02"
    },
    {
        "criterion": "redistributive_conservation",
        "description": "A+B=1",
        "status": 1,
        "evidence": "Experiments 03-04"
    },
    {
        "criterion": "isotropic_axis",
        "description": "Repeated recovery of pi/4 = 45 degrees",
        "status": 1,
        "evidence": "Experiments 03,04,05,09,10,11,12"
    },
    {
        "criterion": "coupling_gap",
        "description": "G=A*B reaches maximum at isotropic balance",
        "status": 1,
        "evidence": "Experiments 03-04"
    },
    {
        "criterion": "partial_coupling_breakdown",
        "description": "Moving away from pi/4 preserves conservation but produces imbalance",
        "status": 1,
        "evidence": "Experiment 05"
    },
    {
        "criterion": "circle_ellipse_transition",
        "description": "Perfect coupling maps to circle; partial coupling maps to ellipse",
        "status": 1,
        "evidence": "Experiment 06"
    },
    {
        "criterion": "bifocality",
        "description": "Partial coupling creates focal separation",
        "status": 1,
        "evidence": "Experiment 07"
    },
    {
        "criterion": "coupling_cost_bridge",
        "description": "A residual bridge grows with focal separation",
        "status": 1,
        "evidence": "Experiment 08"
    },
    {
        "criterion": "orthogonal_signature",
        "description": "Complementary orientation satisfies theta + phi = 90 degrees",
        "status": 1,
        "evidence": "Experiment 09"
    },
    {
        "criterion": "trace_balance",
        "description": "Normal and tangent traces balance at pi/4",
        "status": 1,
        "evidence": "Experiment 10"
    },
    {
        "criterion": "tangent_plane_origin",
        "description": "Tangent-plane coordinates cross origin at pi/4",
        "status": 1,
        "evidence": "Experiment 11"
    },
]

df = pd.DataFrame(criteria)

score = df["status"].sum()
total = len(df)
score_ratio = score / total

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)

FIG_OUT.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(10, 5))
plt.bar(df["criterion"], df["status"])
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 1.2)
plt.ylabel("criterion recovered")
plt.title("Experiment 13 — Object Identification Criteria")
plt.tight_layout()
plt.savefig(FIG_OUT)
plt.close()


with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 13 — Object Identification\n\n")

    f.write("Identification criteria:\n\n")

    for _, r in df.iterrows():
        f.write(
            f"[{int(r['status'])}] {r['criterion']}\n"
            f"    {r['description']}\n"
            f"    evidence: {r['evidence']}\n\n"
        )

    f.write("Score:\n")
    f.write(f"criteria_recovered = {score}/{total}\n")
    f.write(f"score_ratio        = {score_ratio:.6f}\n\n")

    f.write("Identification:\n")
    f.write(
        "The reconstructed structure satisfies the minimal criteria for a "
        "single coupled geometric architecture. It contains conservation, "
        "complementarity, coupling, isotropic balance, partial-coupling "
        "breakdown, bifocality, residual bridging, orthogonal projection, "
        "trace balance, and tangent-plane crossing.\n\n"
    )

    f.write("GEO interpretation:\n")
    f.write(
        "Within the GEO research language, this architecture is identified as "
        "the geometric coupling object underlying the later GEO effective law. "
        "Its interpretation as a geometric superconductor architecture is a "
        "model-level identification, not yet an independent physical proof.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 13 — Object Identification")
print()
print(f"criteria_recovered = {score}/{total}")
print(f"score_ratio        = {score_ratio:.6f}")
print()
print("Identification:")
print("single coupled geometric architecture recovered")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_OUT)
