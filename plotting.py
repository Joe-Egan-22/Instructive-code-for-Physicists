# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:35:40 2024

@author: josep

This details plotting, for different plots, see DIFFERENT PLOTS image in the folder.

For basic plot commands, look for the image in the folder.

See DISPLAYING for different ways to see the plot.
"""

import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(100)
y_values = x_values**2

fig = plt.figure()
ax = fig.add_subplot(221) #subplot made in first row, first collumn of the first figure
ax.text(2.5,7.5,'1st plot')


ax.plot(x_values, y_values,linewidth = 3, label='y=3x',linestyle='solid') # arrays must be same size (same shape?), note the line width parameter and label

#linestyles include, dotted, solid, dashed, dashdot

ax.set_xlabel('x-label ()', fontsize=18)
ax.set_ylabel('y-label ()', fontsize=16)# different font sizes
ax.set_title('Plot Title',fontsize=18,color='blue') # can change the colour of labels, note the american spelling

ax1 = fig.add_subplot(222)
ax1.plot(x_values, 3*x_values)
ax1.text(2.5,40,'2nd plot',rotation=90)

ax2 = fig.add_subplot(223)
ax2.plot(x_values, x_values**3)
ax2.set_xlabel('3rd plot')

ax3 = fig.add_subplot(224)
ax3.plot(x_values,np.sqrt(x_values))
ax3.set_xlabel('4th plot')

fig.tight_layout(pad=1.0)

ax.legend(loc='upper left')
plt.savefig('example_plot.png',dpi=300)
plt.show()
plt.close()

'''
FINAL NOTE

To add mathmatical symbols into titles/labels, use LaTeX notation and surround it with $...$.

'''



