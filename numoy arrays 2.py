# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:46:18 2024

@author: josep

This details the creation and slicing of N-dimensional numpy arrays.

First, look at the ARRAY INDEXING picture in the folder.

Will only use 3D array because principles apply to any order of array.
"""

import numpy as np

ARRAY = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],
                  [[19,20,21],[22,23,24],[25,26,27]]])

#printing this array, we see it is a 3d array of three 3x3 arrays

SECOND_MATRIX = ARRAY[1]

MAT2_ROW3 = ARRAY[1,2]

MAT2_COL2 = ARRAY[1,:,1] # the collon selects everything on the axis it refers too (in this case all rows in collumn 1)

ROW2_ALL = ARRAY[:,1] # can be [:,1,:]

SPECIFIC = ARRAY[2,1,0] #third matrix, second row, first element

#you get the picture, just experiment here if you need to check an array