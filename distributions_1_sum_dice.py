#!/usr/bin/env python3
import sys
import numpy as np
import random
import scipy as sp
import sklearn as skl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


dice_5times_6sides_100=[]
for i in range(100):
    dice=[random.randint(1,6) for n in range(5)]
    dice_5times_6sides_100.append(sum(dice))

y_100,x_100=np.histogram(dice_5times_6sides_100,range=(5,30),bins=25)

print(sp.stats.kstest(dice_5times_6sides_100,'norm'))

dice_5times_6sides_10000=[]
for i in range(10000):
    dice=[random.randint(1,6) for n in range(5)]
    dice_5times_6sides_10000.append(sum(dice))

y_10k,x_10k=np.histogram(dice_5times_6sides_10000,range=(5,30),bins=25)

print(sp.stats.kstest(dice_5times_6sides_10000,'norm'))

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



random_5times_100=[]
for i in range(100):
    dice=[random.random() for n in range(5)]
    random_5times_100.append(sum(dice))

print(sp.stats.kstest(random_5times_100,'norm'))

random_5times_10000=[]
for i in range(10000):
    dice=[random.random() for n in range(5)]
    random_5times_10000.append(sum(dice))

print(sp.stats.kstest(random_5times_10000,'norm'))

random_normal_10000=[]
for i in range(10000):
    dice=np.random.normal()
    random_normal_10000.append(dice)

print(sp.stats.kstest(random_normal_10000,'norm'))