# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:38:48 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("QuizMeasurements.csv",dtype='float',delimiter=',',skip_header=0)

c1 = np.array(data[:,0])