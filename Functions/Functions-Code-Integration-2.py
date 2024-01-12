#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:15:08 2021

@author: rebeccacorley
"""
#import required libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate  


#import data and print
print("The raw data is: \n")
function_real = np.genfromtxt('function_real.dat', delimiter = ' ')
print(function_real, '\n') #prints raw data

#convert raw data to a list to allow sorting/integrating - it is stored as an array because of genfromtxt
print("The raw data is converted to a list")
f = function_real.tolist()

#f is a list of (x,y) values [list of lists], must unzip
x,y = zip(*f)

#plot to check
plt.scatter(x,y, marker="*", color="g")
plt.show()

#sort raw data from smallest to largest
f.sort(key=lambda l: l[0])

#This function checks and prints some of the data at the beginning and end of data set for sorting
print("The data is sorted from least to greatest: \n")
for i in range(len(f)):
    if i<5 or len(f)-i<=5:
        print(i, ": ", f[i])
print()

#unzip the sorted list
x,y=zip(*f)

#line plot of definite integral to compare to previous plot
plt.plot(x,y, 'g-', label="Definite Integral")
plt.legend(loc="upper left")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#use trapezodial rule to integrate the data
print("The value of pi squared: ", np.pi*np.pi)
definite_int = np.trapz(y,x)
print("Value of definite integral: ", definite_int)
print("The error between pi squared and the definite integral is: ", abs(np.pi*np.pi - definite_int))
#use cumulative trapezoidal rule for indefinite integral
indefinite_int = integrate.cumtrapz(y, x, initial=0)
print("The indefinite integral gives: \n", indefinite_int)
#plot for indefinite integral
plt.plot(x, indefinite_int, color='purple', label="Indefinite Integral")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="upper left")
plt.show()
