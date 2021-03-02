import pandas as pd
import numpy as np
from scipy.stats import bernoulli, geom, binom, poisson

import seaborn as sns
import matplotlib.pyplot as plt


rv = bernoulli(0.5)
print(sum(rv.rvs(size=100)))
print(rv.pmf(1))
print(rv.pmf(0))

rv = geom(0.1)
df = pd.DataFrame({
    "k": list(range(1, 21)),
    "PMF": [rv.pmf(k) for k in range(1, 21)]
})
sns.barplot(data=df, x="k", y="PMF")
plt.tight_layout()
plt.savefig("geom.png", dpi=300)
plt.close()

n = 100
p = 0.05
rv = binom(n, p)
df = pd.DataFrame({
    "k": list(range(0, n + 1)),
    "PMF": [rv.pmf(k) for k in range(0, n + 1)]
})
sns.barplot(data=df, x="k", y="PMF")
plt.tight_layout()
plt.savefig("binom.png", dpi=300)
plt.close()

rv = poisson(50)
df = pd.DataFrame({
    "k": list(range(0, 100)),
    "PMF": [rv.pmf(k) for k in range(0, 100)]
})
sns.barplot(data=df, x="k", y="PMF")
plt.tight_layout()
plt.savefig("poisson.png", dpi=300)
plt.close()


def maximum_success_series(sample):
    max_series = 0
    current_series = 0
    for k in sample:
        if k == 1:
            current_series += 1
        else:
            if current_series > max_series:
                max_series = current_series

            current_series = 0
    
    return max_series


n = 100
p = 0.5
N = 10000
rv = bernoulli(0.5)

counts = {}
values = []
for i in range(N):
    sample = rv.rvs(size=n, random_state=32)
    k = maximum_success_series(sample)
    counts[k] = counts.get(k, 0) + 1
    values.append(k)

print(counts)
print(values)
print(np.mean(values))

df = pd.DataFrame({
    "k": [k for k in counts.keys()],
    "freq": [counts[k] / N for k in counts.keys()]
})

sns.barplot(data=df, x="k", y="freq")
plt.tight_layout()
plt.savefig("max_success_series.png", dpi=300)
plt.close()
