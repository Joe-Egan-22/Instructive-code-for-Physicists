# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:43:02 2024

@author: josep

This details how to write a get variable function which validates any errors.
"""

#funtion to get a number

def get_number():
    while True: #we need the while true bit
        try:
            number = float(input('Enter a number between 0 and 50: ')) # we make sure the input is instantly converted to a float to catch any value errors.
            if number < 0 or number > 50: #enter any conditions you need in if statements
                print('Enter number in the requested range')
            else:
                break #make sure to add at the end of the try part
        
        except ValueError: #we can add multiple excepts to catch different errors
            print('Input a number')
    return number

#funtion to get a string

def get_string():
    while True:
        try:
            string = str(input('enter a four-letter word: '))
            if len(string) == 0:
                print('Enter something')
            elif string.isnumeric() == False  and string.isalpha() == False:
                print('Seriously?')
            elif string.isnumeric():
                print('Words do not contain numbers.')
            elif len(string) != 4:
                print('Word needs to be four letters long.') 
            else:
                break
        except Exception: #This is a more versatile way of catching a variety of errors
            print('Need valid input')
    return string


#num = get_number()
#print('The number is {0:f}'.format(num))

print('Four letter word is',get_string())

