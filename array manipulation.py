# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:17:02 2024

@author: josep

This details how numpy arrays can be manipulated.
"""

import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

array3 = np.hstack((array1,array2)) #stacks arrays along second axis, both must have same dimensions apart from this axis

#note the double brackets

#for 2D arrays:

array4 = np.array([[1],[2],[3]])
array5 = np.array([[4],[5],[6]])

array6 = np.hstack((array4,array5))

#vstack stacks rows, thus the number of collumns and other dimensions must be the same

array7 = np.vstack((array1,array2))

array8 = np.vstack((array4,array5))

#dstack stacks arrays along the third axis (by depth). As always, all dimensions apart from depth must be the same

array9 = np.dstack((array1,array2))

array10 = np.dstack((array4,array5))

#the np.reshape function changes the dimensions of an array, useful if you want to stack them a specific way

array11 = array7

array12 = np.reshape(array11,(3,2)) #note the syntax here
array13 = np.reshape(array11,6) #must reshape to have same total number of elements

#finally the np.hsplit function splits an array by collumns, wheres vsplit splits it by rows

array14 = np.arange(0,16)
array15 = np.reshape(array14,(4,4))

array16 = np.hsplit(array15,2) # second number is how many collumns/rows the array is divided into, must be an equal division
array17 = np.vsplit(array15,2)