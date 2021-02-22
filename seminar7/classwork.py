import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)
gl = pd.read_csv("gene_lengths.tsv", sep="\t", index_col=0).sort_index()
size_factors = [0.35219656, 0.39439086, 0.73057344, 1.66138079, 1.60002838, 1.48313616, 1.28046971, 0.92434274, 1.59306799, 1.34997698]

RPK = df.div(gl["Length"] / 10**3, axis=0)
TPM = RPK.div(RPK.sum(axis=0) / 10**6, axis=1)

RPM = df.div(df.sum(axis=0) / 10**6, axis=1)
RPKM = RPM.div(gl["Length"] / 10**3, axis=0)

TPM = TPM.div(size_factors, axis=1)
RPKM = RPKM.div(size_factors, axis=1)

RPKM = np.log2(RPKM + 1)
RPKM = RPKM.loc[RPKM.max(axis=1) > 0]

RPKM["median"] = RPKM.median(axis=1)
RPKM = RPKM.sort_values("median", ascending=False)
RPKM = RPKM.iloc[:10000]

RPKM["fold change"] = RPKM.iloc[:, :5].mean(axis=1) - RPKM.iloc[:, 5:10].mean(axis=1)
RPKM["abs fold change"] = np.abs(RPKM["fold change"])
RPKM = RPKM.sort_values("abs fold change", ascending=False)

RPKM_tumor = RPKM.iloc[:5, :5].T
RPKM_normal = RPKM.iloc[:5, 5:10].T

RPKM_tumor = RPKM_tumor.melt(var_name="Gene", value_name="Expression")
RPKM_tumor["Type"] = "Tumor"
RPKM_normal = RPKM_normal.melt(var_name="Gene", value_name="Expression")
RPKM_normal["Type"] = "Normal"
RPKM = pd.concat([RPKM_tumor, RPKM_normal])

sns.barplot(data=RPKM, x="Gene", y="Expression", hue="Type")
plt.tight_layout()
plt.savefig("test.pdf")
