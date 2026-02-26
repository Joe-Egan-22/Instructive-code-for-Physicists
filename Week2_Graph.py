# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:27:32 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.array([8.79,18.79,28.79,38.79])
y = np.array([0.64,0.31,0.28,0.14])

a,b = np.polyfit(1/x,y,1)

plt.xlabel('1/mass/g^-1') # creates a label 'x' for the x-axis
plt.ylabel('height/m') # creates a label 'y' for the y-axis
plt.title('Relation of mass to maximum height') # gives the plot a title
plt.scatter(1/x,y) # Create plot
plt.plot(1/x,a*1/x+b)
plt.grid()
plt.show() # Show the plot


z = ((y/(1/(x/1000)))*2*9.81/0.019**2)

print([z])

print(a/1000*2*9.81/0.019**2)

print((438.12-295.15)/2)