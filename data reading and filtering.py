# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:48:15 2024

@author: josep

This details how to read and filter data from a file.

NOTE THIS CODE DOES NOT WORK AS THERE IS NO FILE. This just gives the process
you need to read and filter a data file.
"""

import numpy as np

x = np.array([])
y = np.array([])

file = open('file name','r')
for line in file:
    _line = line.strip('\n') #gets rid of whitespace between each line
    if (_line[0] != '%' and len(_line) > 0): #makes sure line is not a comment and that it contains something
        print(_line)
        print(_line.split())
        try:
            x_data = float(_line.split()[0])
            y_data = float(_line.split()[1]) #splits lines into x and y data
            x = np.append(x, x_data)
            y = np.append(y, y_data) #adds data to arrays
        except ValueError as e:
            print(e)
            print('Cannot convert float...', _line) #catches any value errors
            
file.close() #ALWAYS REMEMBER THIS!!!!

print("Size of two arrays = ", x.size, y.size)

'''
ADD CODE FOR REMOVING LINES CONTAINING STUFF WE DON'T NEED

CODE IS ON ASSIGNMENT 2 FROM SEM1
'''