"""
DHRUV PATEL 
AM.EN.U4CSE16507
"""

import numpy as np 
import matplotlib.pyplot as plt 

#Task No.1 - Histogram1
t1 = np.random.poisson(5,1000)
plt.hist(t1,10,density=True,edgecolor="black")
plt.show()

#Task No.1 - Histogram2
t2 = np.random.poisson(10,1000)
plt.hist(t2,15,density=True,edgecolor="red")
plt.show()

#Task No.1 - Histogram3
t3 = np.random.poisson(15,1000)
plt.hist(t3,20,density=True,edgecolor="green")
plt.show()

