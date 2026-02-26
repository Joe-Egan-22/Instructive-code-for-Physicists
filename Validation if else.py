# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:11:01 2024

@author: josep

This covers validation. This allows errors to be recognised and caught by the
program instead of it shitting itself. These errors which are searched for are
called exceptions.

There is a list of exceptions in the folder with this code. Some common examples
are checking that data or an input are within a certain range or that there are
no infinities (nans) or zeros. Another example is checking whether an input is
the required type.

Remember that they like you to include these and include as many as you can.
"""

#validation with if-else

x_string = input('Enter first integer: ')
y_string = input('Enter second integer: ')

if x_string.isnumeric():
    if y_string.isnumeric:
        x_integer = int(x_string)
        y_integer = int(y_string)
        
        if y_integer != 0:
            number_division = x_integer / y_integer
            print('first divided by second is {}'.format(number_division))
        
        else:
            print('Denominator should be non-zero')
    else:
        print('Input y_string is non-numeric')
else:
    print('Input x_string is non-numeric')