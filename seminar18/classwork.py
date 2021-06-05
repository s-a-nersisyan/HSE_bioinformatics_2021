import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, RidgeCV, Lasso, LassoCV

N = 20
x = np.linspace(-5, 5, N)
y = 3*x - 1 + np.random.normal(scale=10, size=N)
sns.scatterplot(x=x, y=y)

X = np.column_stack([
    x**i for i in range(N)
])
model = LinearRegression(fit_intercept=False)
model.fit(X, y)
print(model.score(X, y))

print(model.coef_)
print(model.intercept_)


x = np.linspace(-5, 5, 1000)
X = np.column_stack([
    x**i for i in range(N)
])
y_pred = model.predict(X)
sns.lineplot(x=x, y=y_pred)
plt.ylim([-10, 10])

plt.tight_layout()
plt.savefig("test.pdf")


df1 = pd.read_csv("TCGA-COAD_gene.csv", index_col=0).T
df2 = pd.read_csv("TCGA-COAD_miRNA.csv", index_col=0).T

X = -df2.to_numpy()
y = df1["ZEB1"].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17)

model = LassoCV(positive=True)
model.fit(X_train, y_train)
print(model.coef_)

res = pd.DataFrame({"miRNA": df2.columns, "coef": model.coef_})
res = res.loc[res["coef"] != 0]
print(res.sort_values("coef"))

print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
