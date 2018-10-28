"""
DHRUV PATEL 
AM.EN.U4CSE16507
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import random


x=np.random.normal(1,0.5,1000)
y=np.random.poisson(5,1000)
l=[]
for k in range(100):
    h=np.random.randint(x)
    j=np.random.rand(y)
    for i in range(100):
        l.append((h[i] + j[i])/2)

plt.hist(l,normed=True)
plt.show()

