import pandas as pd
import numpy as np

from sklearn.datasets import *

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV


# How to make numpy arrays from pandas dataframe
df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()

# Load data
X, y = load_wine(return_X_y=True)
# Split into training set (80%) and test set(20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=17
)

# Define and fit the model
model = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", KNeighborsClassifier(n_neighbors=5, weights="distance", p=1))
])
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))

# We can repeat the code above 100 times
# using k-fold cross-validation. This will
# result in distribution of accuracies, from
# which we can calculate mean, std, quantiles etc.
accuracies = cross_val_score(
    model, X, y, 
    scoring=make_scorer(accuracy_score),
    cv=RepeatedStratifiedKFold(n_repeats=100)
)
print(np.mean(accuracies), np.std(accuracies))

# Cross-validation can also be used to select
# global hypermarameters
params = {
    "clf__n_neighbors": [1, 3, 5, 7],
    "clf__weights": ["uniform", "distance"],
    "clf__p": [1, 2]
}

cv = GridSearchCV(
    model, params,
    scoring=make_scorer(accuracy_score),
    cv=RepeatedStratifiedKFold(n_repeats=10)
)
cv.fit(X, y)
print(cv.best_params_)
print(cv.best_score_)
