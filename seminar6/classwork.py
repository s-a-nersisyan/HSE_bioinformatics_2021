import pandas as pd

df = pd.DataFrame([[1, 17.17, "qwerty"], [-10, 0.1, "hello"], [0, 10.10, "world"], [-100, 0.32, "hi"]])
print(df)
df.columns = ["A", "B", "Long column name"]
print(df)
print(df["A"])
print(df.A)
print(df[["A", "Long column name"]])
df["C"] = [-1, -3, -2, -1717]
print(df)
df = pd.DataFrame({
    "A": [1, -10, 0, -100], 
    "B": [17.17, 0.1, 10.10, 0.32], 
    "Long column name": ["qwerty", "hello", "world", "hi"]
})
print(df)
df.index = ["P", "Q", "R", "S"]
print(df)
print(df.loc[["R", "P"], ["B", "Long column name"]])
print(df.loc["R", "A"])
df.loc["New row"] = [0, -100, "yoyoyo"]
print(df)
print(df.iloc[0:2, 0:2])

df.to_csv("our_table.csv")
df.to_csv("our_table.tsv", sep="\t")

df = pd.read_csv("TCGA-COAD.tsv", sep="\t", index_col=0)
print(df)
print(df.loc[(df["TCGA-A6-2675-11A"] > 1000) & (df["TCGA-A6-2671-11A"] < 1000), "TCGA-F4-6704-11A"])
print(df.loc["A1BG"] * df.loc["A1BG"] + df.loc["A1BG-AS1"])
print(df.loc[df.median(axis=1) > 2])

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=df, x="TCGA-A6-2675-11A", y="TCGA-A6-2671-11A")
plt.tight_layout()
plt.savefig("test1.pdf")
plt.close()

df = df.loc[["CD24", "FOXM1", "RACGAP1"]]
df = df.T
print(df)
df = df.melt(var_name="Gene", value_name="Expression")
print(df)

sns.barplot(data=df, x="Gene", y="Expression")
plt.tight_layout()
plt.savefig("test2.pdf")
