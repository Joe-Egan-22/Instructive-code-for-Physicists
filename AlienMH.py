# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:47:16 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("AlienMHData.txt",dtype='float',delimiter=',',skip_header=0)

mass = np.array(data[:,0])
height = np.array(data[:,1])

plt.plot(mass,height,'ro', label="measured data") # make a plot of yvals versus xvals using a red circle for each point
plt.plot(height,mass,'g--',label="calculated values") # make a plot of yvals versus xvals using a green dashed line

#plt.plot(data[:,0],data[:,1])
plt.show()