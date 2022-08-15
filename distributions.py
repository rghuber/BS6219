#!/usr/bin/env python3
import numpy as np
import random
import scipy as sp
import sklearn as skl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# BINOMIAL EXAMPLE

dice_5times_6sides_100=[]
for i in range(100):
    dice=[random.randint(1,6) for n in range(5)]
    dice_5times_6sides_100.append(sum(dice))

y_100,x_100=np.histogram(dice_5times_6sides_100,range=(5,30),bins=25)

dice_5times_6sides_10000=[]
for i in range(10000):
    dice=[random.randint(1,6) for n in range(5)]
    dice_5times_6sides_10000.append(sum(dice))

y_10k,x_10k=np.histogram(dice_5times_6sides_10000,range=(5,30),bins=25)

plt.figure(1,figsize=(24,12))

plt.subplot2grid((1,2),(0,0))
plt.title("5 Dice, 6 Sides, 100 rolls")
plt.xticks(range(5,31))
plt.bar(x_100[1:],y_100,color='k',width=0.8)
plt.xlabel("Sum")
plt.ylabel("Count")

plt.subplot2grid((1,2),(0,1))
plt.title("5 Dice, 6 Sides, 10000 rolls")
plt.xticks(range(5,31))
plt.bar(x_10k[1:],y_10k,color='k',width=0.8)
plt.xlabel("Sum")
plt.ylabel("Count")

plt.savefig("dice_5times_6sides.pdf",format='pdf',dpi=300)

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

plt.figure(1,figsize=(24,12))

plt.subplot2grid((1,2),(0,0))
plt.title("D6*D6*D20, 100 rolls")
plt.xticks(range(1,720,100))
plt.bar(x_100[1:],y_100,color='k',width=0.8)
plt.xlabel("Sum")
plt.ylabel("Count")

plt.subplot2grid((1,2),(0,1))
plt.title("D6*D6*D20, 10000 rolls")
plt.xticks(range(1,720,100))
plt.bar(x_100k[1:],y_100k,color='k',width=0.8)
plt.xlabel("Sum")
plt.ylabel("Count")

plt.savefig("dice_product.pdf",format='pdf',dpi=300)