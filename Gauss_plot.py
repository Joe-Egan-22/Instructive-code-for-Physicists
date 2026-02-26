# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:42:07 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('APTexp1_data.txt', dtype='float',delimiter=',', skip_header=1)


blue = np.array(data[:,0])
pink = np.array(data[:,1])
mu = np.mean(blue)  # assign the value of mu
sigma = 0.8  # assign the value of sigma
sigmatrue = np.std(blue)
x = np.linspace(80,100,1000)  # make an array containing 1000 values evenly spaced from 0 to 10

#weighted mean funciton
dm = 0.01*10**-3
dh = 0.02
dx = 0.004
m = 9.52*10**-3
x = 0.03
h = np.array(blue/100)
N = 2*m*9.81*h
D = x**2
k = np.array(N/D)
a = dm/m
b = np.array(dh/h)
c = 2*dx/x
dk = np.array(k*np.sqrt(a**2+b**2+c**2))
W = np.array(k/dk**2)
dW = np.array(1/dk**2)

Weight = np.sum(W)/np.sum(dW)
dWeight = np.sqrt(1/np.sum(dW))

# Now calculate the y values - do this step by step:
S1 = 1.0/(sigma * np.sqrt(2.0 * np.pi))  # this is the first part of the expression
S2 = (x - mu)**2  # this is the numerator of the exponential factor, 
# without the overall negative sign
S3 = - S2 / (2.0 * sigma**2)  # this is the exponential factor
y = S1 * np.exp(S3) # this is the final result

# Now calculate the y values - do this step by step:
S1 = 1.0/(sigmatrue * np.sqrt(2.0 * np.pi))  # this is the first part of the expression
S2 = (x - mu)**2  # this is the numerator of the exponential factor, 
# without the overall negative sign
S3 = - S2 / (2.0 * sigmatrue**2)  # this is the exponential factor
y2 = S1 * np.exp(S3) # this is the final result

# The following lines make a plot and save a copy.
plt.xlabel('x') # creates a label 'x' for the x-axis
plt.ylabel('y') # creates a label 'y' for the y-axis
plt.title('The Gaussian Function') # gives the plot a title
plt.plot(x,y) # plot y versus x
plt.plot(x,y2)
plt.savefig('GaussPlot.png', dpi=600)  # save a copy of the plot
plt.show()


