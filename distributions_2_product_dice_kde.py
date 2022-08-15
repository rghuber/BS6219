#!/usr/bin/env python3
import sys
import numpy as np
import random
import scipy as sp
import sklearn as skl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# POISSON EXAMPLE

dice_product_100=[]
for i in range(100):
    dice=random.randint(1,6)*random.randint(1,6)*random.randint(1,20)
    dice_product_100.append(dice)

y_100,x_100=np.histogram(dice_product_100,range=(1,720),bins=720)

dice_product_100k=[]
for i in range(100000):
    dice=random.randint(1,6)*random.randint(1,6)*random.randint(1,20)
    dice_product_100k.append(dice)

y_100k,x_100k=np.histogram(dice_product_100k,range=(1,720),bins=720)

kernel=sp.stats.gaussian_kde(dice_product_100k)
x_kde=np.linspace(1,720,7200)
y_kde=kernel(x_kde)

plt.figure(1,figsize=(36,12))

plt.subplot2grid((1,3),(0,0))
plt.title("D6*D6*D20, 100 rolls")
plt.xticks(range(1,720,100))
plt.bar(x_100[1:],y_100,color='k',width=0.8)
plt.xlabel("Product")
plt.ylabel("Count")

plt.subplot2grid((1,3),(0,1))
plt.title("D6*D6*D20, 10000 rolls")
plt.xticks(range(1,720,100))
plt.bar(x_100k[1:],y_100k,color='k',width=0.8)
plt.xlabel("Product")
plt.ylabel("Count")

plt.subplot2grid((1,3),(0,2))
plt.title("D6*D6*D20, 10000 rolls, KDE")
plt.xticks(range(1,720,100))
plt.fill_between(x_kde,y_kde,alpha=0.5)
plt.xlabel("Product")
plt.ylabel("Density Estimate")

plt.savefig("dice_product.pdf",format='pdf',dpi=300)

plt.savefig("dice_product.pdf",format='pdf',dpi=300)