# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:09:45 2024

@author: josep

This details how to use lambda functions. Should try to include these to
reduce code length.

NOTE: these should not be assigned to variables, in this case a normal function
should be defined.
"""

#basic structure of a lambda function is:
# lambda a, b : a + b
#so arguments, followed by function

'''
Try doing some here, these are often used to do an operation on all elements of a list
or as an input algorithm, as opposed to defining many functions.
'''

power_list = [lambda x:1, lambda x:x, lambda x:x**2, lambda x:x**3]

x_cubed = power_list[3](2)


def my_map(func, list):
    result = []
    for i in list:
        transform = func(i)
        result.append(transform)  
    return result

nums = [1,2,3,4,5]

print(my_map(lambda x: x+1,nums))

#can add if-else statements into these, instead of using elif, need to do it this way or use normal function

g = (lambda x: x*10 if x > 10 else (x*5 if x < 5 else x))(11)


'''
We pass lambda functions to higher-order functions, which accept functions as arguments.
Examples will be listed alone.
'''

array = [33, 3, 22, 2, 11, 1]
filter(lambda x: x > 10,array)

#this creates an object, to get an iterable from this, we pass object to list(), tuple(), set(), sorted(), frozenset()

sort = sorted(filter(lambda x: x > 10,array))

#map function applies an operation to each element of a list, needs to be passed like the filter function

mapped = tuple(map(lambda x: x**2, array))

'''
Include pandas stuff? I think this allows you to create databases?
'''

import pandas as pd

df = pd.DataFrame({'col1': [1,2,3,4,5,], 'col2': [0,0,0,0,0]})
print(df)

df['col3'] = df['col1'].map(lambda x: x*10) #can replace map with apply

print(df)

df['col4'] = df['col3'].apply(lambda x: 30 if x < 30 else x)

print(df)

'''
Reduce functions take lambda arguments and lists like the previous functions.

This function operates on the first two elements, save the answer and then operates
on the saved result and next item, returning a scalar value.

Does not need to be passed.
'''

