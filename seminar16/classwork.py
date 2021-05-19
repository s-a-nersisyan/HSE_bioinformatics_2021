import pandas as pd
import numpy as np

from sklearn.datasets import make_circles
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_roc_curve

import seaborn as sns
import matplotlib.pyplot as plt


# First, see how C can influence SVM line
np.random.seed(17)

N = 50
X1 = np.random.normal(loc=0, size=(N, 2))
X2 = np.random.normal(loc=3, size=(N, 2))
X = np.vstack([X1, X2])
y = np.array([0]*N + [1]*N)

sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y)

for C in [0.01, 100]:
    model = SVC(kernel="linear", C=C)
    model.fit(X, y)

    w = model.coef_[0]
    b = model.intercept_[0]
    
    xx = np.array([np.min(X[:, 0]), np.max(X[:, 0])])
    yy = (-w[0] * xx - b) / w[1]
    plt.plot(xx, yy)

plt.savefig("test.png", dpi=300)

# RBF kernel
X, y = make_circles(n_samples=100, factor=0.8, noise=0.1)
X1 = np.random.normal(loc=5, size=(100, 2))
X = np.vstack([X, X1])
y = np.hstack([y, [1]*100])

model = SVC(kernel="rbf", C=10000)
model.fit(X, y)
y_pred = model.predict(X)
print(accuracy_score(y, y_pred))

XX, YY = np.meshgrid(
    np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 100),
    np.linspace(np.min(X[:, 1]), np.max(X[:, 1]), 100)
)
Z = model.decision_function(np.c_[XX.ravel(), YY.ravel()])
Z = Z.reshape(XX.shape)
plt.pcolormesh(XX, YY, Z > 0)


sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y)
plt.savefig("test.png", dpi=300)

# TPR, TNR
df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
df = df.loc[df["Subtype"].isin(["Luminal A", "Luminal B"]), ["PGR", "MKI67"," Subtype"]]

X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=17)
model = SVC(kernel="linear")

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))
M = confusion_matrix(y_test, y_pred)
print(M)
TPR = M[0, 0] / (M[0, 0] + M[0, 1])
TNR = M[1, 1] / (M[1, 0] + M[1, 1])
print(TPR, TNR)

plot_roc_curve(model, X_test, y_test)
plt.plot(1 - TPR, TNR, "x", c="red")
plt.savefig("test.png", dpi=300)
