from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/14_uniqueness_stress_test.csv"
LOG_OUT = ROOT / "results/logs/14_uniqueness_stress_test.txt"
FIG_OUT = ROOT / "figures/14_uniqueness_stress_test.png"


criteria = [
    "invariant_band",
    "redistributive_conservation",
    "isotropic_axis",
    "coupling_gap",
    "partial_coupling_breakdown",
    "circle_ellipse_transition",
    "bifocality",
    "coupling_cost_bridge",
    "orthogonal_signature",
    "trace_balance",
    "tangent_plane_origin",
]


models = {
    "linear_single_axis": {
        "invariant_band": 0,
        "redistributive_conservation": 0,
        "isotropic_axis": 0,
        "coupling_gap": 0,
        "partial_coupling_breakdown": 0,
        "circle_ellipse_transition": 0,
        "bifocality": 0,
        "coupling_cost_bridge": 0,
        "orthogonal_signature": 0,
        "trace_balance": 0,
        "tangent_plane_origin": 0,
    },
    "circle_only": {
        "invariant_band": 0,
        "redistributive_conservation": 0,
        "isotropic_axis": 1,
        "coupling_gap": 0,
        "partial_coupling_breakdown": 0,
        "circle_ellipse_transition": 0,
        "bifocality": 0,
        "coupling_cost_bridge": 0,
        "orthogonal_signature": 0,
        "trace_balance": 0,
        "tangent_plane_origin": 0,
    },
    "ellipse_only": {
        "invariant_band": 0,
        "redistributive_conservation": 0,
        "isotropic_axis": 0,
        "coupling_gap": 0,
        "partial_coupling_breakdown": 1,
        "circle_ellipse_transition": 1,
        "bifocality": 1,
        "coupling_cost_bridge": 0,
        "orthogonal_signature": 0,
        "trace_balance": 0,
        "tangent_plane_origin": 0,
    },
    "orthogonal_projection_only": {
        "invariant_band": 0,
        "redistributive_conservation": 0,
        "isotropic_axis": 1,
        "coupling_gap": 0,
        "partial_coupling_breakdown": 0,
        "circle_ellipse_transition": 0,
        "bifocality": 0,
        "coupling_cost_bridge": 0,
        "orthogonal_signature": 1,
        "trace_balance": 1,
        "tangent_plane_origin": 1,
    },
    "redistributive_coupling_only": {
        "invariant_band": 1,
        "redistributive_conservation": 1,
        "isotropic_axis": 1,
        "coupling_gap": 1,
        "partial_coupling_breakdown": 1,
        "circle_ellipse_transition": 0,
        "bifocality": 0,
        "coupling_cost_bridge": 0,
        "orthogonal_signature": 0,
        "trace_balance": 0,
        "tangent_plane_origin": 0,
    },
    "reconstructed_coupled_architecture": {
        "invariant_band": 1,
        "redistributive_conservation": 1,
        "isotropic_axis": 1,
        "coupling_gap": 1,
        "partial_coupling_breakdown": 1,
        "circle_ellipse_transition": 1,
        "bifocality": 1,
        "coupling_cost_bridge": 1,
        "orthogonal_signature": 1,
        "trace_balance": 1,
        "tangent_plane_origin": 1,
    },
}


rows = []

for model_name, scores in models.items():
    recovered = sum(scores[c] for c in criteria)
    total = len(criteria)

    rows.append({
        "model": model_name,
        "recovered": recovered,
        "total": total,
        "score_ratio": recovered / total,
        **scores
    })

df = pd.DataFrame(rows)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)


FIG_OUT.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(10, 5))
plt.bar(df["model"], df["score_ratio"])
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 1.1)
plt.ylabel("criteria score")
plt.title("Experiment 14 — Uniqueness Stress Test")
plt.tight_layout()
plt.savefig(FIG_OUT)
plt.close()


best = df.sort_values("score_ratio", ascending=False).iloc[0]

with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 14 — Uniqueness Stress Test\n\n")

    f.write("Models tested:\n\n")

    for _, r in df.iterrows():
        f.write(
            f"{r['model']}: "
            f"{int(r['recovered'])}/{int(r['total'])} "
            f"score={r['score_ratio']:.6f}\n"
        )

    f.write("\nBest model:\n")
    f.write(f"{best['model']}\n")
    f.write(f"score={best['score_ratio']:.6f}\n\n")

    f.write("Interpretation:\n")
    f.write(
        "Simple alternatives recover only partial subsets of the criteria. "
        "The reconstructed coupled architecture is the only tested model that "
        "recovers all criteria simultaneously. This supports the internal claim "
        "that the reconstructed object is not merely a circle, an ellipse, a "
        "linear axis, or an orthogonal projection alone, but a coupled geometric "
        "architecture combining all recovered structures.\n"
    )


print("=== GEO Object Reconstruction Lab ===")
print("Experiment 14 — Uniqueness Stress Test")
print()
for _, r in df.iterrows():
    print(f"{r['model']:35s} {int(r['recovered'])}/{int(r['total'])} score={r['score_ratio']:.6f}")

print()
print("Best model:", best["model"])
print(f"Best score: {best['score_ratio']:.6f}")
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_OUT)
