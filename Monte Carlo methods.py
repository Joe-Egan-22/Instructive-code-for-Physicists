# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:12:47 2024

@author: josep

This details Monte-Carlo methods. These rely on random sampling to simulate random
physical and mathematical systems.

"Numerical integration, optimistion and sampling from multi-dimensional probability
distributions."

Example we are using here is the estimation of pi, see how in the image in the folder.
"""

import numpy as np
import matplotlib.pyplot as plt

N=10000
nc_x, nc_y = np.array([]), np.array([])
ns_x, ns_y = np.array([]), np.array([])

fig = plt.figure(figsize=[5.0,5.0])
ax = fig.add_subplot(111)

for i in np.arange(0,N,1):
    x_values = np.random.uniform(-1.0,1.0)
    y_values = np.random.uniform(-1.0,1.0)
    
    if ((x_values**2 + y_values**2) <= 1.0):
        nc_x = np.append(nc_x, x_values)
        nc_y = np.append(nc_y, y_values)
    else:
        ns_x = np.append(ns_x, x_values)
        ns_y = np.append(ns_y, y_values)
        
ms = 2
ax.scatter(nc_x, nc_y, c='r', s=ms)
ax.scatter(ns_x, ns_y, c='b', s=ms)

pi = 4*nc_x.size/N
plt.title(pi)

plt.show()