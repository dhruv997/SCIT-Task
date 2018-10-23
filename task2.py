"""
DHRUV PATEL 
AM.EN.U4CSE16507
"""

import numpy as np 
import matplotlib.pyplot as plt 

#Task No.2 - Histogram1
t1 = np.random.normal(5,1000)
plt.hist(t1,5,density=True,edgecolor="black")
plt.show()

#Task No.2 - Histogram2
t2 = np.random.normal(10,1000)
plt.hist(t2,10,density=True,edgecolor="red")
plt.show()

#Task No.2 - Histogram3
t3 = np.random.normal(15,1000)
plt.hist(t3,15,density=True,edgecolor="green")
plt.show()

