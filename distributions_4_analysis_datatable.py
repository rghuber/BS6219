#!/usr/bin/env python3
import sys
import numpy as np
import random
import scipy as sp
import sklearn as skl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd

df=pd.read_csv("titanic.csv")

print(df.describe())
age=df["Age"].dropna().to_list()

age_dist=sp.stats.gaussian_kde(age)

plt.figure(1,figsize=(12,12))
plt.fill_between(np.linspace(1,100,200),age_dist(np.linspace(1,100,200)),alpha=0.5)
plt.savefig("age_distribution.pdf",format='pdf',dpi=300)
