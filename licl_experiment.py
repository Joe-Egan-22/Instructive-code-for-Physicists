# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:06:29 2023

@author: josep
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('licl_data.txt',dtype='float',delimiter=',',skip_header=1)
theta = np.array(data[:,0])
i = np.array(data[:,1])
sigmai = np.array(data[:,2])
thetarad = np.array(theta*np.pi/180)
angles = np.linspace(0,2*np.pi,1000)
ct = np.cos(2*theta*np.pi/180)

avtheta = np.mean(ct)
sigma_I = 0.05
avi = np.mean(i)
avtheta2 = np.mean(ct**2)
avthetai = np.mean(ct*i)
m = (avthetai-avtheta*avi)/(avtheta2-avtheta**2)
c = (avi*avtheta2-avthetai*avtheta)/(avtheta2-avtheta**2)
g = np.array((m*ct+c-i))
G = np.sum(g**2)
x = np.linspace(-1,1,1000)
y = m*x+c
sigma_g = 1/len(data)*(1/(avtheta2-avtheta**2))*sigma_I**2
sigma_c = 1/len(data)*(avtheta2/(avtheta2-avtheta**2))*sigma_I**2

chi2 = np.sum((g/sigma_I)**2)


plt.title('An Experiment to Investigate the Reflective Properties of Lithium Chloride')
plt.xlabel('cos(2theta)/no units')
plt.ylabel('Intensity/Wm^-2')
plt.errorbar(ct,i,0.05,fmt='rx')
plt.plot(x,y)
plt.show()

print('gradient =',m,'+/-',sigma_g)
print('intercept =',c,'+/-',sigma_c)
print('chi squared =',chi2)
I_2 = c
I_1 = m + c