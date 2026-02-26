# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:27:32 2024

@author: josep

This details the try-except method of validation.

Try-except validation. Runs a defined process if the operation fails in a specific way

"""

x_string = input('Enter first integer: ')
y_string = input('Enter second integer: ')

try:
    
    x_integer = int(x_string)
    y_integer = int(y_string)
    number_division = x_integer / y_integer
    print('first divided by second is {}'.format(number_division))


except: #this is a 'bare' exception, so every exception in the try block executes the code here
    print('something went wrong')
    
except ValueError as e:
    print('Value error')
    print('System error message 1:',e)
    
except ZeroDivisionError() as e:
    print('Value error')
    print('System error message 2:',e)