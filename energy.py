# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:54:02 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt

#variables
m = 0.00879
dl = 0.019
g = 9.81
h = 0.64
u = np.sqrt(2*g*h)
t = np.linspace(0,0.7,1000)
v = u-g*t
H = u*t-1/2*g*t**2
#equation
k = 2*m*g*h/(dl)**2
KE = 1/2*m*v**2
GPE = m*g*H
#results
plt.xlabel('time/s') # creates a label 'x' for the x-axis
plt.ylabel('energy') # creates a label 'y' for the y-axis
plt.title('Relation of KE to GPE') # gives the plot a title
plt.plot(t,KE)
plt.plot(t,GPE)
plt.grid()
plt.show() # Show the plot