import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import pearsonr, spearmanr
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)

print(df)
print(pearsonr(df["UBE2C"], df["ESR1"]))
print(spearmanr(df["UBE2C"], df["ESR1"]))

sns.scatterplot(x="UBE2C", y="ESR1", data=df)
plt.tight_layout()
plt.savefig("UBE2C_vs_ESR1.pdf")
plt.close()

X = spearmanr(df.iloc[:, :50], axis=0)[0]
df = pd.DataFrame(X, index=df.columns[:50], columns=df.columns[:50])

sns.clustermap(df, cmap=sns.color_palette("coolwarm", as_cmap=True), vmin=-1, vmax=1)
plt.savefig("corr_sns.clustermap.pdf")
plt.close()

model = PCA()  # or TSNE()
df[["PC1", "PC2"]] = model.fit_transform(df.iloc[:, :50])[:, :2]
print(df)
print(model.explained_variance_ratio_)

plt.figure(figsize=(10, 10))
sns.scatterplot(x="PC1", y="PC2", hue="Subtype", data=df)
plt.tight_layout()
plt.savefig("PC1_vs_PC2.pdf")
plt.close()
