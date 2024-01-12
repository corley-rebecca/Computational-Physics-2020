#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:15:08 2021

@author: rebeccacorley
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate  


function_real = np.genfromtxt('function_real.dat') #import data
#data2 = np.genfromtxt('function_unknown.dat')

#print(function_known)
function_real = function_real[np.argsort(function_real[: , 0])] #sorts x-values in data from smallest to largest
print(function_real)


integrate_function_real = np.trapz(function_real[:, 1], function_real[:, 0])
#print("Area: " +str(integrate_function_real))

y_int  = integrate.cumulative_trapezoid(function_real[:,1], function_real[1,:], dx=1.0)

plt.scatter([x[0] for x in function_real], [x[1] for  x in function_real], marker="*")
plt.show()
#plt.scatter([x[0] for x in data2], [x[1] for  x in data2], marker=".", color="g")
#plt.show()

'''
x = np.linspace(-2, 2, num=20)
y = x
y_int = integrate.cumulative_trapezoid(y, x, initial=0)
plt.plot(x, y_int, 'ro', x, y[0] + 0.5 * x**2, 'b-')
plt.show()

'''