# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:18:24 2023

@author: josep
"""

import numpy as np

x = np.array([8.79,18.79,28.79,38.79])
y = np.array([0.64,0.31,0.28,0.14])

MeanVal = np.mean(y)  #calculate mean value of this set
StDev = np.std(y)  # calculate the standard deviation of this set

print("mean = ", MeanVal)  # print out the mean.
print("standard deviation = ", StDev)  # print out the standard deviation.