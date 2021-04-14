import pandas as pd
import numpy as np

from scipy.stats import ttest_ind, shapiro

df = pd.read_csv("colon_cancer_tumor_vs_normal_unpaired_FPKM.tsv", sep="\t", index_col=0)

df["LFC"] = df.iloc[:, :5].mean(axis=1) - df.iloc[:, 5:10].mean(axis=1)
df = df.sort_values("LFC")
print(df)

print(df.loc["DPEP1"])
print(ttest_ind(df.loc["DPEP1"].iloc[0:5], df.loc["DPEP1"].iloc[5:10]))

df["p-value"] = [ttest_ind(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index]
df = df.sort_values("p-value")
print(df)

df = pd.read_csv("breast_cancer_key_genes.tsv", sep="\t", index_col=0)
print(df)
print(shapiro(df["MKI67"].iloc[0:100]))
