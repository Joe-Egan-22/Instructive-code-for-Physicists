# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:52:35 2024

@author: josep

This details how to read data files.
"""

import numpy as np
tangents = np.array([])


input_file = open('sine_data.txt','r')
for line in input_file:
    line_no_return = line.strip('\n')
    line_elements = line_no_return.split(',')
    
    if line_elements[0] != '#':
        angle = float(line_elements[0])
        tan_value = np.tan(np.deg2rad(angle))
        if tan_value != np.inf:
            tangents = np.append(tangents, tan_value)
            
input_file.close()
print(tangents)