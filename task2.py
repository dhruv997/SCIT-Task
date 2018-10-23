"""
DHRUV PATEL 
AM.EN.U4CSE16507
"""

import numpy as np 
import matplotlib.pyplot as plt 

#Task No.2 - Histogram 1
t1 = np.random.normal(5,2,1000)					#mean=5,std=2,event=1000
plt.title("Histogram of Task 2 Graph 1")
plt.xlabel('Events')
plt.ylabel('Probability density')
plt.hist(t1,5,density=True,edgecolor="black")
plt.show()

#Task No.2 - Histogram 2
t2 = np.random.normal(10,3,1000)				#mean=10,std=3,event=1000
plt.title("Histogram of Task 2 Graph 2")
plt.xlabel('Events')
plt.ylabel('Probability density')
plt.hist(t2,10,density=True,edgecolor="red")
plt.show()

#Task No.2 - Histogram 3
t3 = np.random.normal(15,4,1000)				#mean=15,std=4,event=1000
plt.title("Histogram of Task 2 Graph 3")
plt.xlabel('Events')
plt.ylabel('Probability density')
plt.hist(t3,15,density=True,edgecolor="green")
plt.show()

