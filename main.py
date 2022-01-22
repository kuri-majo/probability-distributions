from math import gamma
from turtle import title
from scipy.stats import uniform
import seaborn as sns

# random numbers from uniform distribution
n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc = start, scale=width)

g = sns.displot(
    data=data_uniform,
    bins=20,
    stat="proportion",
    kde=True,
    palette="crest",
    line_kws={"linewidth": 4},
    )
g.set(title="Uniform Distribution")