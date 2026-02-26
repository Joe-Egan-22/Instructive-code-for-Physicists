# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:49:09 2024

@author: josep

This details how to use genfrom txt.

NOTE THIS CODE WILL NOT WORK AS THERE IS NO FILE, just shows all the stuff you
can do.
"""

import numpy as np

data = np.genfromtxt('FILE NAME', delimiter = 'DELIMETER', dtype = 'TYPE', comments = '%', skip_header = X)

#maybe allow the user to input the delimeter, comment, dtype they want in a consol.