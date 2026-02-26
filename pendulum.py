# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:36:20 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("ManyMeasurements.csv",dtype='float',delimiter=',',skip_header=1)

times = np.array(data[:,0])
sigma = np.std(times)
mu = np.mean(times)
pi = np.pi
x = np.linspace(7.3,8.1,1000)
S1 = 1.0/(sigma * np.sqrt(2.0 * np.pi))  # this is the first part of the expression
S2 = (x - mu)**2  # this is the numerator of the exponential factor, 
# without the overall negative sign
S3 = - S2 / (2.0 * sigma**2)  # this is the exponential factor
y = S1 * np.exp(S3) # this is the final result


#plt.hist(times,bins=30,density=2)
#plt.plot(x,y,'k.')
plt.xlabel('times/s')
plt.ylabel('counts')
plt.title('Histogram of pendulum data')
plt.show()