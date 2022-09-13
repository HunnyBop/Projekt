import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_id = input("Please enter the product id: ")

opinions = pd.read_json(f"opinions/{product_id}.json")

opinions_count = len(opinions)
pros_count = opinions["pros"].map(bool).sum()
cons_count = opinions["cons"].map(bool).sum()
average_score = opinions["score"].mean().round(2)

stars_recommendation = pd.crosstab(opinions["rcmd"], opinions["score"], dropna=False)
# print(stars_recommendation)

if not os.path.exists("plots"):
    os.makedirs("plots")

recommendations = opinions["rcmd"].value_counts(
    dropna=False).sort_index().reindex([False, True, None])

recommendations.plot.pie(
    label = "",
    title = "Recommendations: "+product_id,
    labels = ["Not recommend", "Recommend", "No opinion"],
    colors = ["crimson", "forestgreen", "grey"],
    autopct = lambda p: f"{p:.1f}%" if p>0 else ""
)
plt.savefig(f"plots/{product_id}_rcmd.png")
plt.close()

stars = opinions["score"].value_counts(
    dropna=False).sort_index().reindex(np.arange(0,5.5,0.5))

stars.plot.bar(
    label = "",
    title = "Stars score: "+product_id,
    xlabel = "Stars values",
    ylabel = "Opinions count",
    color = "hotpink",
    rot = 0
)
plt.savefig(f"plots/{product_id}_stars.png")
plt.close()