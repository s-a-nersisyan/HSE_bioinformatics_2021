import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, balanced_accuracy_score

import matplotlib.pyplot as plt

df = pd.read_pickle("bc_data.pkl")
ann = pd.read_pickle("bc_ann.pkl")

genes = "TRIP13;UBE2C;ZWINT;EPN3;KIF4A;ECHDC2;MTFR1;STARD13;IGFBP6;NUMA1;CCNL2".split(";")
df = df[genes]

X_train = df.loc[ann.loc[ann["Dataset type"] == "Training"].index].to_numpy()
y_train = ann.loc[ann["Dataset type"] == "Training", "Class"].to_numpy()

X_test = df.loc[ann.loc[ann["Dataset type"] == "Validation"].index].to_numpy()
y_test = ann.loc[ann["Dataset type"] == "Validation", "Class"].to_numpy()

res = pd.DataFrame(columns=["max_depth", "train_BA", "test_BA"])
for max_depth in range(1, 20):
    #model = DecisionTreeClassifier(max_depth=max_depth, class_weight="balanced", random_state=17)
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=max_depth,
        class_weight="balanced",
        random_state=17
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_train)
    train_BA = balanced_accuracy_score(y_train, y_pred)

    y_pred = model.predict(X_test)
    test_BA = balanced_accuracy_score(y_test, y_pred)
    
    res.loc[len(res)] = [max_depth, train_BA, test_BA]

print(res)

# Uncomment for DecisionTreeClassifier
#plt.figure(figsize=(20, 20))
#plot_tree(model, feature_names=df.columns, fontsize=3)
#plt.savefig("test.png", dpi=300)
