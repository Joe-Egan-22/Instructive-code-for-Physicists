# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:41:25 2023

@author: josep
"""
import numpy as np

data = np.genfromtxt("AlienMHData.txt",dtype='float',delimiter=',',skip_header=0)

print(data)
