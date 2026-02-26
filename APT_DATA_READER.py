# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:32:20 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('APT_DATA.txt',dtype='float',delimiter=',',skip_header=1)
ap = np.array([17.723 , 17.611 , 17.610 , 17.624 , 17.620 , 17.417 , 17.910 , 17.429 , 17.633 , 17.510 , 17.615 , 17.618 , 17.623])
ap2 = np.array([20.300 , 20.400 , 19.800 , 20.400 , 20.700 , 19.900])
h1 = np.array(data[:,0])
h2 = np.array(data[:,1])
se = 0.05
mu1 = np.mean(h1)
mu2 = np.mean(h2)
sd1 = np.std(h1)
sde = 0.05
sd2 = np.std(h2)
sigmam1 = sd1/np.sqrt(10)
sigmam2 = sd2/np.sqrt(10)
pi = np.pi
mop = np.mean(ap)
mos = np.std(ap)
emop = mop/np.sqrt(13)
x = np.linspace(80,90,1000)
ans = np.std(ap)
ans2 = np.std(ap2)
anp2 = ans2/np.sqrt(6)

# Now calculate the y values - do this step by step:
S1 = 1.0/(sde * np.sqrt(2.0 * np.pi))  # this is the first part of the expression
S2 = (x - mu1)**2  # this is the numerator of the exponential factor, 
# without the overall negative sign
S3 = - S2 / (2.0 * sde**2)  # this is the exponential factor
y = S1 * np.exp(S3) # this is the final result


# Now calculate the y values - do this step by step:
S1 = 1.0/(sd1 * np.sqrt(2.0 * np.pi))  # this is the first part of the expression
S2 = (x - mu1)**2  # this is the numerator of the exponential factor, 
# without the overall negative sign
S3 = - S2 / (2.0 * sd1**2)  # this is the exponential factor
y1 = S1 * np.exp(S3) # this is the final result





# The following lines make a plot and save a copy.
plt.xlabel('x') # creates a label 'x' for the x-axis
plt.ylabel('y') # creates a label 'y' for the y-axis
plt.title('The Gaussian Function') # gives the plot a title
plt.plot(x,y) # plot y versus x
plt.plot(x,y1)
#plt.savefig('GaussPlot.png', dpi=600)  # save a copy of the plot
plt.show()