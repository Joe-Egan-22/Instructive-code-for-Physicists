# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:37:35 2024

@author: josep

Basic input and print program. Reminder that number inputs should be converted
to floats in order to perform operations on them. Also shows how to add floats
to the print statement

"""

greeting = 'Hello '

name_input = input('What is your name? ')

question = ' How are you'

print(greeting + name_input + question + '?\n')

number_string = input("Enter a number: ")

number_float = float(number_string)

transform = number_float * 5

print(number_string + ' when transformed is',transform)