# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:57:12 2024

@author: josep

This details how to write external files. First see the FILES picture
in the folder to learn about different opening modes.
"""

import numpy as np

example_file = open('example_file.txt','w') #note the file name, extension and mode with which it is opened, in this case writing

example_file.write('hello world 1') #files with the same name get overwritten so be careful with that too
example_file.close()

"""
ALWAYS CLOSE THE FILE!!! OR BAD THINGS WILL HAPPEN TO YOUR FAMILY! 
"""

#variables can also be added to the file

example_file = open('example_file.txt','w')
my_string = 'hello world 2'
example_file.write(my_string)
example_file.close()

#strings can also be printed into files

example_file = open('example_file.txt','w')
#my_string2 = 'hello world 3'
#print(my_string2, file=example_file)
example_file.close()

#for loops can be used to write files, line by line

angles = np.arange(0,182,2)
angles_radians = np.deg2rad(angles)
sines = np.sin(angles_radians)

sine_file = open('sine_data.txt','w')

print('# angle (degree), sine value',file=sine_file)

for index in range(len(sines)):
    print(angles[index],sines[index])
    
    print('{0:.2f},{1:.3f}'.format(angles[index],sines[index]),file=sine_file)
    
sine_file.close()

"""
see FILE LOOP METHODS image in folder for other ways to do this.
"""
