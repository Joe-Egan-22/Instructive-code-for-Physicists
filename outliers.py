# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:03:26 2024

@author: josep

This code details how to filter outliers.

CODE WILL NOT WORK AS THERE IS NO DATA FILE.
"""

import numpy as np

x_cont = np.arange(0,25,1000) #example 'continuous' x array

x = np.arange(25)
y = np.arange(25)

y_predicted = 2*x_cont**2 + 3*x_cont + 4 #this is an example of a predicted curve that will fit your data
outlier_indices = np.where(np.abs(y - y_predicted) > 5) #5 is an example number, this creates a tuple of the indices 
                                                        #which correspond to outliers.
                                                        
x_subset = x[outlier_indices]
y_subset = y[outlier_indices]

'''
It is recommended that you plot your outliers as well as clean data, just make outliers visible
this is why we have the subset lists.
'''

x_ok = np.delete(x, outlier_indices)
y_ok = np.delete(y, outlier_indices)#these arrays have the outliers removed, curves should be fitted to these 
                                    #data and any quantities (chi squared, curve parameters, standard dev) 
                                    #calculated based off of these.
                                    
'''
IMPORTANT POINT!!!

If you have a 3-collumned numpy array (using the genfromtxt function for example)

When deleting outlier indices, you need to specify to delete along axis=0, otherwise will
screw up.

'''
