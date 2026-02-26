# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 21:13:42 2024

@author: josep

This shows how to format (insert stuff into strings), note that pylint
 suggests a different way, WHICH YOU SHOULD ADD HERE ALSO.
"""

INSERT = 'whatever you want'

print('Formatting allows you to insert stuff into brackets like this: {0}'.format(INSERT))

#{} brackets are the replacement fields, the numbers indicate with variables in the format statement go where

print('Here are three things: {0}, {1}, {2}'.format(1,2,3)) #try altering the green numbers

#note that these do not have to be numbers in the replacement fields

LONG_NUMBER = 2/3

print('{0} can be rounded to {0:4.3f}'.format(LONG_NUMBER))

#formatting also allows you to define precision, must define total numbers, number of decimals
#and the format specifier at the end (f, g, e/E, etc). Should revise what each does.