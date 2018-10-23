"""
DHRUV PATEL 
AM.EN.U4CSE16507
"""

import numpy as np 
import matplotlib.pyplot as plt 

#Task No.1 - Histogram 1
t1 = np.random.poisson(5,1000)		  			#mean=5,event=1000
plt.title("Histogram of Task 1 Graph 1")
plt.xlabel('Events')
plt.ylabel('Probability density')
plt.hist(t1,10,density=True,edgecolor="black")
plt.show()

#Task No.1 - Histogram 2
t2 = np.random.poisson(10,1000)					#mean=10,event=1000
plt.title("Histogram of Task 1 Graph 2")
plt.xlabel('Events')
plt.ylabel('Probability density')
plt.hist(t2,15,density=True,edgecolor="red")
plt.show()

#Task No.1 - Histogram 3
t3 = np.random.poisson(15,1000)					#mean=15,event=1000
plt.title("Histogram of Task 1 Graph 3")
plt.xlabel('Events')
plt.ylabel('Probability density')
plt.hist(t3,20,density=True,edgecolor="green")
plt.show()

