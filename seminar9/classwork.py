from scipy.stats import uniform, norm, binom
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rv = uniform(1, 16)
print(rv.rvs(size=100))
print(rv.pdf(197))

mu = 4
sigma = 2
rv = norm(mu, sigma)

df = pd.DataFrame()
df["x"] = np.linspace(mu - 5*sigma, mu + 5*sigma, 1000)
df["PDF(x)"] = rv.pdf(df["x"])

sns.lineplot(data=df, x="x", y="PDF(x)")
plt.tight_layout()
plt.savefig("test1.pdf")
plt.close()

n = 100
p = 0.2

rv1 = binom(n, p)
mu = n*p
sigma = np.sqrt(n * p * (1 - p))
rv2 = norm(mu, sigma)

df1 = pd.DataFrame()
df1["k"] = list(range(0, n + 1))
df1["PMF(k)"] = rv1.pmf(df1["k"])

sns.barplot(x="k", y="PMF(k)", data=df1)

df2 = pd.DataFrame()
df2["x"] = np.linspace(mu - 5*sigma, mu + 5*sigma, 1000)
df2["PDF(x)"] = rv2.pdf(df2["x"])
sns.lineplot(data=df2, x="x", y="PDF(x)")

plt.tight_layout()
plt.savefig("test2.pdf")
plt.close()

rv = uniform(0, 1)
x = rv.rvs(size=1000000)
f = 4 * np.sqrt(1 - x**2)
print(np.mean(f))
