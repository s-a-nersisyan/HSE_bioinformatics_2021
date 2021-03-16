import pandas as pd
import numpy as np

from scipy.stats import t, norm, poisson

import seaborn as sns
import matplotlib.pyplot as plt

rv1 = t(1)
rv2 = norm(0, 1)

df1 = pd.DataFrame({"Sample": rv1.rvs(size=100), "Distr": "t(1)"})
df2 = pd.DataFrame({"Sample": rv2.rvs(size=100), "Distr": "norm(0, 1)"})
df = pd.concat([df1, df2])

sns.stripplot(data=df, x="Distr", y="Sample")
plt.tight_layout()
plt.savefig("test.pdf")

sns.histplot(data=df2, x="Sample", stat="density")

df = pd.DataFrame({"x": np.linspace(-3, 3, 1000)})
df["PDF"] = rv2.pdf(df["x"])
sns.lineplot(data=df, x="x", y="PDF")

plt.tight_layout()
plt.savefig("t_vs_norm.pdf")
plt.close()

l = 17
n = 100
rv = poisson(l)

vals = []
for i in range(10000):
    sample = rv.rvs(size=n)
    s = (np.mean(sample) - l) * np.sqrt(n / l)
    vals.append(s)

sns.histplot(x=vals, stat="density")

df = pd.DataFrame({"x": np.linspace(-3, 3, 1000)})
df["PDF"] = norm(0, 1).pdf(df["x"])
sns.lineplot(data=df, x="x", y="PDF")

plt.tight_layout()
plt.savefig("poisson_CLT.pdf")
plt.close()

# Dean rating problem
print((norm(0, 1).ppf(0.975) / 0.02)**2)
