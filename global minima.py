# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:46:27 2024

@author: josep

This details how to find the global minima.
"""

import numpy as np
import matplotlib.pyplot as plt
'''
1) Random values method. Think things need to be added to this code to make it work??
'''

X_START = -2.0
STEP_SIZE = 0.3
TOLERANCE = 0.001

NUMBER_OF_SEARCHES = 3
SEARCH_MIN = -3
SEARCH_MAX = 3

def function(x_variable):
    return x_variable**4 - 4 * x_variable**2 + 2 * x_variable    
    
def random_start():
    return SEARCH_MIN + np.random.rand() * (SEARCH_MAX - SEARCH_MIN)

def hill_climbing(x_minimum=X_START, step=STEP_SIZE):
    """
    Runs 1D hill climbing algorithm with varying step size
    """
    difference = 1
    minimum = function(x_minimum)
    counter = 0

    while difference > TOLERANCE:
        counter += 1
        minimum_test_minus = function(x_minimum - step)
        minimum_test_plus = function(x_minimum + step)
        if minimum_test_minus < minimum:
            x_minimum -= step
            difference = minimum - minimum_test_minus
            minimum = function(x_minimum)
        elif function(x_minimum + step) < minimum:
            x_minimum += step
            difference = minimum - minimum_test_plus
            minimum = function(x_minimum)
        else:
            step = step * 0.1

    return x_minimum, minimum, counter

def plot_result(x_minimum, starting_values):
    """
    Plots function and result
    """
    x_values = np.linspace(-3, 3, 100)

    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('f(x)', fontsize=14)

    
    ax.plot(x_values, function(x_values),'r-',label=r'$f(x) = x^4 - 4x^2 + 2x$')
    ax.scatter(starting_values, function(starting_values), label=r'$x_0$',
                 color='black')
    ax.scatter(x_minimum, function(x_minimum),
                 label=r'$x_{{min}} = {0:.2f}$'.format(x_minimum), color='blue')
    #ax.scatter([-1.52], [-6.94], color='k', label='Min at x=-1.52')
    #ax.scatter([1.28], [-1.31], color='b', label='Min at x=1.28')
                 
    ax.legend()
    plt.show()
    return None

def main():
    starting_values = np.array([X_START])
    x_minimum, minimum, count = hill_climbing() #might need to make an algorithm for this?
    searches = 1
    while searches < NUMBER_OF_SEARCHES:
        searches += 1
        x_start = random_start()
        starting_values = np.append(starting_values, x_start)
        (x_minimum_test, minimum_test, count_temp) = hill_climbing(x_minimum=x_start)
        
        if minimum_test < minimum:
            minimum = minimum_test
            x_minimum = x_minimum_test
        count += count_temp
        
    plot_result(x_minimum, starting_values)
    return 0

'''
fminbound method
'''

from scipy.optimize import fmin, fminbound

def function(x):
    return np.sin(x) + np.cos(x*np.sqrt(2)) + np.sin(x*np.sqrt(3))

global_minima_f_value = 999.9
global_minima_x_value = 999.9
x_start = np.linspace(-4,4,100)
for i, v in enumerate(x_start):
    result = fmin(function, [v], full_output = True, disp = False)
    if (result[1] < global_minima_f_value):
        global_minima_f_value = result[1]
        global_minima_x_value = result[0][0]
        
print('minima:',global_minima_f_value, global_minima_x_value)

result = fminbound(function,-3, 0, full_output=True, disp=False)

print('results:',result)

'''
Basinhopping method, this apparently doesn't work always? Maybe use the fminbound.
'''

from scipy.optimize import basinhopping

x0 = 4
result_bh = basinhopping(function, x0, minimizer_kwargs={'method':'BFGS'},niter=1000)

print(result_bh.x, result_bh.fun)


    