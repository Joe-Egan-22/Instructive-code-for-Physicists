# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:13:21 2024

@author: josep

Functions and how to do write and do stuff with them.

REMEMBER: local variables are only called inside functions and should be defined
in lower (snake) case. Global variables can be called anywhere and should be defined
in capitals.
"""

NUMBER_STRING = input('Enter a number: ')
NUMBER_FLOAT = float(NUMBER_STRING)
def function_name(input_arguments):
    '''
    This is the auto-generated caption. Add a short description of what the
    function does and replace the sections in CAPS.

    Parameters
    ----------
    input_arguments : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    return_value = 1 #this is just an example
    
    return return_value

def hello_user(user):
    """
    Greets user

    Parameters
    ----------
    user : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    greeting = 'Hello ' + user
    print(greeting)
    
    return None

def logic_function(bool1, bool2):
    '''
    

    Parameters
    ----------
    bool1 : TYPE
        DESCRIPTION.
    bool2 : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    return (bool1 or bool2) and not (bool1 and bool2)
    
if logic_function(True, False):
    print('this is true')
    
print('outside of if statement')

def captain_obvious(number):
    '''
    

    Parameters
    ----------
    number : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    if number > 100:
        print('That number is greater than 100.')
        
        if number > 1000:
            print('...and greater than 1000')
    
    elif number <= 10:
        print('That number is less than or equal to 10.')
        
    else:
        print('This number is between 10 and 100')
    return None
    

hello_user('Name')
captain_obvious(NUMBER_FLOAT)

