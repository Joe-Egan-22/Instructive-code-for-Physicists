# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:48:37 2024

@author: josep

This details how to use random numbers.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_gaussian():
    data = np.random.normal(1, 5, 500)
    plt.hist(data, bins=10, density=True, alpha=0.6, color='r')
    text = 'mean:',np.mean(data),'std:',np.std(data)
    plt.title(text,fontsize=16)
    
    plt.show()
    
np.random.seed() #no argument gives random seed each time
plot_gaussian()

np.random.seed(1234) #fixed seed and sequence
plot_gaussian()
