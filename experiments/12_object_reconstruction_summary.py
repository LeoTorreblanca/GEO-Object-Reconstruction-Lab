from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/12_object_reconstruction_summary.csv"
LOG_OUT = ROOT / "results/logs/12_object_reconstruction_summary.txt"
FIG_OUT = ROOT / "figures/12_pi4_convergence.png"

rows = [
    {
        "experiment": "03_coupling_geometry",
        "property": "maximum coupling gap",
        "axis_deg": 45.0,
        "evidence": "A=B=0.5, G=A*B=0.25"
    },
    {
        "experiment": "04_redistributive_geometry",
        "property": "redistributive conservation",
        "axis_deg": 45.0,
        "evidence": "A+B=1, gap maximum at pi/4"
    },
    {
        "experiment": "05_coupling_breakdown",
        "property": "perfect coherence",
        "axis_deg": 45.0,
        "evidence": "coherence=1, imbalance=0"
    },
    {
        "experiment": "09_orthogonal_signature",
        "property": "orthogonal balance",
        "axis_deg": 45.0,
        "evidence": "theta = 90-theta"
    },
    {
        "experiment": "10_shadow_trace",
        "property": "trace balance",
        "axis_deg": 45.0,
        "evidence": "S_normal=S_tangent=0.5"
    },
    {
        "experiment": "11_tangent_plane_model",
        "property": "tangent-plane origin",
        "axis_deg": 45.0,
        "evidence": "x_plane=0, y_plane=0"
    },
]

df = pd.DataFrame(rows)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)

plt.figure(figsize=(10, 5))
plt.scatter(df["experiment"], df["axis_deg"])
plt.axhline(45.0, linestyle="--")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Recovered axis (degrees)")
plt.title("Experiment 12 — Convergence Toward pi/4")
plt.tight_layout()

FIG_OUT.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(FIG_OUT)
plt.close()

with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 12 — Object Reconstruction Summary\n\n")

    f.write("Recovered convergences:\n\n")

    for _, r in df.iterrows():
        f.write(
            f"{r['experiment']} | "
            f"{r['property']} | "
            f"axis={r['axis_deg']:.6f} deg | "
            f"{r['evidence']}\n"
        )

    f.write("\nCurrent reconstruction status:\n\n")
    f.write("The laboratory has reconstructed the following properties:\n")
    f.write("- original invariant band: 3/4, sqrt(3/5), pi/4\n")
    f.write("- redistributive conservation: A+B=1\n")
    f.write("- maximum coupling at pi/4\n")
    f.write("- coherence loss away from pi/4\n")
    f.write("- circle-to-ellipse transition\n")
    f.write("- bifocal separation under partial coupling\n")
    f.write("- coupling cost bridge between foci\n")
    f.write("- orthogonal signature\n")
    f.write("- shadow trace balance\n")
    f.write("- tangent-plane coordinate crossing\n\n")

    f.write("Interpretation:\n")
    f.write(
        "Multiple independent reconstructions converge on the same isotropic "
        "axis, pi/4. The object has not yet been named as a final physical entity, "
        "but the recovered structure already satisfies the minimal requirements "
        "of a coupled geometric architecture with conservation, complementarity, "
        "projection, bifocality, and tangent-plane trace behavior.\n"
    )

print("=== GEO Object Reconstruction Lab ===")
print("Experiment 12 — Object Reconstruction Summary")
print()
print("Convergences recovered:", len(df))
print("All recovered axes:", sorted(df["axis_deg"].unique()))
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_OUT)
