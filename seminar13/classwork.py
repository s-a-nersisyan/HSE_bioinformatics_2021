import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, rankdata, mannwhitneyu

df = pd.DataFrame(np.random.normal(size=(100, 10)))
df["p-value"] = ttest_ind(df.iloc[:, :5], df.iloc[:, 5:], axis=1)[1]

df["padj"] = np.minimum(df["p-value"] * len(df) / rankdata(df["p-value"]), 1)
df = df.sort_values("padj")
print(df)

df = pd.read_csv("colon_cancer_tumor_vs_normal_unpaired_FPKM.tsv", sep="\t", index_col=0)
print(df.loc["FABP6"])
print(df.loc["ETV4"])
print(mannwhitneyu(df.loc["FABP6"].iloc[:5], df.loc["FABP6"].iloc[5:]))
print(mannwhitneyu(df.loc["ETV4"].iloc[:5], df.loc["ETV4"].iloc[5:]))
