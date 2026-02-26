# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:41:42 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("ManyMeasurements.csv",dtype='float',delimiter=',',skip_header=1)

x = np.linspace(0,10,10)
mn = np.mean(data[:,0])
sigma = np.std(data[:,0])