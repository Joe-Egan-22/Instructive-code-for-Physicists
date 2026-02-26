# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:36:12 2024

@author: josep

This details file reading and editing.
"""

countries_file = open('countries.txt','r')

list_of_countries = []

for line in countries_file: #files are iterable by their lines
    line = line.strip('\n') #when printing each line there is an unseen return (\n in print statements), this line gets rid of them
    print(line)
    list_of_countries.append(line)
    
countries_file.close()

list_of_countries.sort(reverse = True)

output_file = open('countries_upper_case.txt','w')

print('% list of countries in upper case', file = output_file)

for country in list_of_countries:
    print(country.upper(), file=output_file)
    
output_file.close()