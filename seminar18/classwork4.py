import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, RidgeCV, Lasso, LassoCV

df1 = pd.read_csv("TCGA-COAD_gene.csv", index_col=0).T
df2 = pd.read_csv("TCGA-COAD_miRNA.csv", index_col=0).T

X = -df2.to_numpy()
y = df1["CD44"].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=17
)

model = LassoCV(positive=True)
model.fit(X, y)
print(model.score(X, y))

res = pd.DataFrame({"miRNA": df2.columns, "coef": -model.coef_})
res = res.loc[res["coef"] != 0]
res = res.sort_values("coef")
print(res)
