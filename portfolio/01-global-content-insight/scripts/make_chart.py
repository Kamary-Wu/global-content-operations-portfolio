from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
data = pd.read_csv(ROOT / "data" / "hallyu_associations.csv")
data = data.sort_values("percentage")

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=160)
bars = ax.barh(data["association"], data["percentage"], color="#E84A5F")

fig.suptitle("K-pop is the leading association with Korea", x=0.18, y=0.97, ha="left", fontsize=15, weight="bold")
fig.text(0.18, 0.91, "Share of responses in the 2024 Overseas Hallyu Survey", fontsize=10, color="#555555")
ax.set_xlabel("Share of responses (%)")
ax.set_xlim(0, 20)
ax.grid(axis="x", color="#DDDDDD", linewidth=0.7)
ax.set_axisbelow(True)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.tick_params(axis="y", length=0)

for bar, value in zip(bars, data["percentage"]):
    ax.text(value + 0.35, bar.get_y() + bar.get_height() / 2, f"{value:.1f}%", va="center", fontsize=10)

fig.text(0.01, 0.01, "Source: Ministry of Culture, Sports and Tourism, Republic of Korea (2024).", fontsize=8, color="#666666")
fig.tight_layout(rect=(0, 0.05, 1, 0.88))

output_dir = ROOT / "assets"
output_dir.mkdir(parents=True, exist_ok=True)
fig.savefig(output_dir / "hallyu_associations.png", bbox_inches="tight", facecolor="white")
fig.savefig(output_dir / "hallyu_associations.svg", bbox_inches="tight", facecolor="white")
