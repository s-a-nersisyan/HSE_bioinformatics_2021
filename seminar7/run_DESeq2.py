import pandas as pd

from rpy2 import robjects
from rpy2.robjects import Formula

from rpy2.robjects import pandas2ri
pandas2ri.activate()

from rpy2.robjects.packages import importr
DESeq2 = importr("DESeq2")

counts = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)
# Technical requirement, never mind
groups = pd.DataFrame({"smth1": ["smth2"] * len(counts.columns)}, index=counts.columns)

# Calculate normalization factors
dds = DESeq2.DESeqDataSetFromMatrix(countData=counts, colData=groups, design=Formula("~ 1"))
dds = DESeq2.estimateSizeFactors_DESeqDataSet(dds)
size_factors = DESeq2.sizeFactors_DESeqDataSet(dds)
print(size_factors)
