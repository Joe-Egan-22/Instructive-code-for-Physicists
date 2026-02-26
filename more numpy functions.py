# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:11:44 2024

@author: josep

This details more useful numpy stuff.
"""

import numpy as np

#numpy has constants e.g.

pi = np.pi
e = np.e

array = np.array([0.0, 1.0, np.pi, np.inf, np.nan])

print(np.isnan(array), np.isinf(array)) #test if number is 'nan' or infinity

print(np.max(array))

print(np.nanmax(array)) #also has np.nanmin()

print(np.nanargmax(array)) #the index of the element which is max and not 'nan'

#np.where() function gives the tuple of INDICES of an array subject to conditions which you set for the elements themselves
#remember that it only returns the indices, even though conditions apply to elements.

array2 = np.arange(0,30,3)

indices = np.where(array2 > 11)

array3 = array2[indices] #use this method to get a desired slice of an array, subject to your conditions

#this function is useful for filtering and validation

array4 = np.where(array2 % 2 == 0, array2**2) #this returns an array where elements are equal to array2 if
                                                #if conditions are met, otherwise will return array^2.
                                                
#note the condition, i think, is that the remainder when divided by 2 must equal zero?