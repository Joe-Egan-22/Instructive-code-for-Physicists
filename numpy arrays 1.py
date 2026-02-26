# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:30:14 2024

@author: josep

This details how to create and use numpy arrays.
"""

import numpy as np

array1 = np.array([]) #note the format

array1 = np.append(array1, [0,1,2,3]) #note the order

array2 = np.arange(1,7,2) #same rules as using range

array_sqrt = np.sqrt(array2)

array_times = array2 * 10

array_min = np.min(array2)

array_max = np.max(array2)