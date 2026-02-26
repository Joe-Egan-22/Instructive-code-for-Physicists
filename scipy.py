# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:53:58 2024

@author: josep

This details the basics of scipy.
"""

import scipy
import numpy as np

#typing help(scipy) gives a list of stuff

import scipy.constants as pc

#pc being physical constants, type dir(pc) for a list of stuff

from scipy import special

special.hermite(1) #these are polynomials, image in folder

from scipy.integrate import quad

def function(x):
    return 2*x**2 + 3*x + 4

integral, error = quad(function, -2, 2) #scipy can integrate, with an error apparently?

from scipy.optimize import fmin

X_START = 1
minimum = fmin(function, X_START, full_output = True, disp = False)

#this finds the minima of a function, to find the maxima, define a new function or lambda function
#which is -1*function.

'''
More often, you will be using a two-parameter function, to minimise this, the only thing you alter 
is putting two starting values AS A TUPLE

so fmin(function, (X_START, Y_START),...)

'''

