# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:10:22 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("SC10LineData.csv",dtype='float',delimiter=',',skip_header=1)

time = np.array(data[:,0])
amp = np.array(data[:,1])
uncert = np.array(data[:,2])

plt.xlabel('time/s')
plt.ylabel('amplitude/cm')
plt.errorbar(time,amp,uncert)