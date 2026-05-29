from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]

CSV_OUT = ROOT / "results/csv/20_final_claim_audit.csv"
LOG_OUT = ROOT / "results/logs/20_final_claim_audit.txt"
FIG_OUT = ROOT / "figures/20_final_claim_audit.png"

claims = [
    ("reconstructed", "signature_band", "3/4, sqrt(3/5), pi/4 form compact band", "Exp 19, 02"),
    ("reconstructed", "redistributive_conservation", "A+B=1 emerges as core conservation law", "Exp 03,04"),
    ("reconstructed", "pi4_axis", "pi/4 recovered across coupling, coherence, trace, tangent plane", "Exp 03,04,05,09,10,11,12"),
    ("reconstructed", "circle_ellipse_transition", "perfect coupling maps to circle; partial coupling maps to ellipse", "Exp 06"),
    ("reconstructed", "bifocality", "partial coupling produces focal separation", "Exp 07"),
    ("reconstructed", "coupling_cost_bridge", "residual bridge grows with focal separation", "Exp 08"),
    ("reconstructed", "orthogonal_signature", "theta + phi = 90 degrees", "Exp 09"),
    ("reconstructed", "shadow_trace", "normal/tangent traces balance at pi/4", "Exp 10"),
    ("reconstructed", "tangent_plane", "tangent-plane coordinates cross origin at pi/4", "Exp 11"),

    ("derived_operator", "eta", "eta=3/5 interpreted as natural active partition", "Exp 15"),
    ("derived_operator", "fc", "fc=sqrt(eta) as causal operational boundary", "Exp 15"),
    ("derived_operator", "B", "B=1-eta as free geometric sector", "Exp 15"),
    ("derived_operator", "Phi", "Phi as coherent transfer depth", "Exp 15,16"),
    ("derived_operator", "alpha", "alpha=Phi*B/sqrt(2), separated conceptual/operational", "Exp 15,16,17"),
    ("derived_operator", "R", "R=eta^(1/3) as operational transfer scale", "Exp 15"),

    ("application_bridge", "hubble_bridge", "operational alpha reconstructs H0 target through explicit operator", "Exp 17"),
    ("application_bridge", "vacuum_gravity_links", "later GEO labs may use these operators as downstream applications", "external labs"),

    ("interpretation", "geometric_coupling_object", "single coupled geometric architecture reconstructed internally", "Exp 13,14,18"),
    ("interpretation", "geometric_superconductor_architecture", "model-level GEO interpretation of the reconstructed object", "Exp 13,18"),
    ("interpretation", "paradigm_shift", "possible long-term implication, not asserted by this lab", "not claimed"),
]

df = pd.DataFrame(
    claims,
    columns=["category", "claim", "statement", "evidence"]
)

category_order = {
    "reconstructed": 4,
    "derived_operator": 3,
    "application_bridge": 2,
    "interpretation": 1,
}

df["audit_weight"] = df["category"].map(category_order)

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV_OUT, index=False)

summary = df.groupby("category").size().reset_index(name="count")

FIG_OUT.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(9, 5))
plt.bar(summary["category"], summary["count"])
plt.xticks(rotation=30, ha="right")
plt.ylabel("number of audited claims")
plt.title("Experiment 20 — Final Claim Audit")
plt.tight_layout()
plt.savefig(FIG_OUT)
plt.close()

with open(LOG_OUT, "w") as f:
    f.write("GEO Object Reconstruction Lab\n")
    f.write("Experiment 20 — Final Claim Audit\n\n")

    f.write("Purpose:\n")
    f.write(
        "This audit separates directly reconstructed results, derived GEO operators, "
        "application bridges, and model-level interpretations. It prevents the lab "
        "from confusing internal reconstruction with external physical validation.\n\n"
    )

    for category in ["reconstructed", "derived_operator", "application_bridge", "interpretation"]:
        f.write(f"[{category.upper()}]\n")
        sub = df[df["category"] == category]

        for _, r in sub.iterrows():
            f.write(
                f"- {r['claim']}: {r['statement']} "
                f"(evidence: {r['evidence']})\n"
            )

        f.write("\n")

    f.write("Final audit statement:\n")
    f.write(
        "The lab directly reconstructs a coupled geometric architecture from "
        "signature emergence, conservation, coupling, bifocality, orthogonal trace, "
        "and tangent-plane behavior. GEO operators are then connected as derived "
        "internal quantities. Hubble/Vacuum/Gravity are downstream application "
        "bridges, not required for the initial object reconstruction. The phrase "
        "'geometric superconductor architecture' is retained as the GEO model-level "
        "interpretation of the reconstructed object, not as an independently proven "
        "physical replacement for existing frameworks.\n"
    )

print("=== GEO Object Reconstruction Lab ===")
print("Experiment 20 — Final Claim Audit")
print()
print(summary.to_string(index=False))
print()
print("CSV :", CSV_OUT)
print("LOG :", LOG_OUT)
print("FIG :", FIG_OUT)
