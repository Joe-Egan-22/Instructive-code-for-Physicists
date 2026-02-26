# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:58:19 2024

@author: josep

This details mesh arrays and contour plots. There is an image in the folder with
some code relating to this.
"""

import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(0,11,2)
y_values = np.arange(1,21,2)

z = x_values**2 + y_values**2

'''
THIS WILL NOT WORK AS ARRAYS ARE DIFFERENT SIZES.

We need to mesh these arrays, there are three methods of doing this...
'''

def meshes_1(x, y):
    x_mesh = np.empty((0,len(x)))
    for i, v in enumerate(y):
        x_mesh = np.vstack((x_mesh, x))
        
    y_mesh = np.empty((0,len(y)))
    for i, v in enumerate(x):
        x_mesh = np.vstack((y_mesh, y))
    y_mesh = np.transpose(y_mesh)
    
    return x_mesh, y_mesh

#try figure out what is happening in meshes_1 for better understanding.

def meshes_2(x,y):
    return np.meshgrid(x,y)

#nothing to add here, numpy just does it for you
    
def meshes_3(x,y):
    dx = x[1]-x[0]
    dy = y[1]-y[0]
    return np.mgrid[slice(np.min(y), np.max(y) + dy, dy),
                    slice(np.min(x), np.max(x) + dx, dx)]

#again, not sure what goes on in this function, try and make sense of it if you need it

fig = plt.figure()
ax = fig.add_subplot(111)
contour_plot = ax.contour(x_mesh, y_mesh, function(x_mesh, y_mesh), 5)
ax.clabel(contour_plot, fontsize=12, colors='r')
ax.set_xlabel('X LABEL')
ax.set_ylabel('Y LABEL')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
contour_plot = ax.contour(x_mesh, y_mesh, function(x_mesh, y_mesh), [81, 225])
ax.clabel(contour_plot, fontsize=12, colors='r')
ax.set_xlabel('X LABEL')
ax.set_ylabel('Y LABEL')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
contour_plot_filled = ax.contour(x_mesh, y_mesh, function(x_mesh, y_mesh), 5)
ax.clabel(contour_plot, fontsize=12, colors='r')
fig.colorbar(contour_plot_filled)
ax.set_xlabel('X LABEL')
ax.set_ylabel('Y LABEL')
plt.show()

'''
When finding minimum chi squared, an extra feature includes doing a contour plot of
the two parameters which generate chi squared. Add the mimimum chi squared to the plot
and an ellipse which corresponds to all the points where you have chi squared + 1. Minimum
chi should lie at the centre and the ellipse defines the uncertainty in that min value

The relevant slides for this are in the folder

'''

