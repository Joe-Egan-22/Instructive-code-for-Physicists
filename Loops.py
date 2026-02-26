# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:55:01 2024

@author: josep

Loops:

Recursive functions call themselves within the function. 

Can also for loops with the 'while' statement, which performs a task until a 
condition is no longer met.

For loops loop through a collection of items, like the elements of a list and
perform an operation for each of those items.

This also details what 'range()' does.
"""

def factorial(number):
    '''
    Example of recursive function to find factorials.

    Parameters
    ----------
    number : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    if number > 1:
        
        return number * factorial(number - 1)
    
    else:
        
        return 1
    
    
#while loop example

COUNTER = 0

while COUNTER <= 5:
    print(COUNTER)
    
    COUNTER += 1 #shorthand for adding 1 to the counter
    
print('while loop terminated\n')

#for loop example

ARRAY = [1,2,3,4,5]

for element in ARRAY:
    print(element)
    
print('For loop terminated') #good practice to include a statement showing the loop is done?


#example of how range works

for i in range(0,1,4): #note that default start is 0, an end value is required
                        #(will NOT include in the range, default step is 1 (step is middle))
    print(i)


    