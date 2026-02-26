# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:21:15 2023

@author: josep
"""

import numpy as np

Angles = [6.0, 12.0, 18.0, 24.0, 36.0]  # our list of incident angles in degrees
n_r = 1.54   # define the refractive index of the glass
n_i = 1.0 # define the refractive index of air

Radangles = np.array(Angles)

Radangles = Radangles*np.pi/180

Isin =  np.sin(Radangles)
Rsin = Isin/n_r

Refangles = np.arcsin(Rsin)*180/np.pi