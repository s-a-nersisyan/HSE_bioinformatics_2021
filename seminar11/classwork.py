import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import norm


df = pd.read_csv("breast_cancer_key_genes.tsv", sep="\t", index_col=0)

df = df.melt(var_name="Gene", value_name="Expression")
sns.violinplot(x="Gene", y="Expression", data=df)
plt.tight_layout()
plt.savefig("violinplot.pdf")
plt.close()

sns.histplot(x=df["ESR1"], stat="density")
sns.kdeplot(x=df["ESR1"])
plt.tight_layout()
plt.savefig("hist.pdf")
plt.close()

mu = df["MKI67"].mean()
sigma = df["MKI67"].std()
rv = norm(mu, sigma)

sns.histplot(x=df["MKI67"], stat="density")
df = pd.DataFrame({"x": np.linspace(df["MKI67"].min(), df["MKI67"].max(), 1000)})
df["p(x)"] = rv.pdf(df["x"])
sns.lineplot(x="x", y="p(x)", data=df)
plt.tight_layout()
plt.savefig("MKI67_norm.pdf")
plt.close()
