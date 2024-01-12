#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:15:56 2021

@author: rebeccacorley
"""
#using given data, implement a method to calculate the derivative 


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 

#import data and print
print("The raw data is: \n")
data = np.genfromtxt('function_real.dat', delimiter = ' ')

#convert to list
data.tolist()

#define empty array to send derivative to
dy_dx=[]

#separate x,y lists
x_values = data[:,0]
y_values = data[:,1]

#sort x list
x_sort = data[np.argsort(data[:,0])]

nbins=200#define number of bins

h = 10 #define h - spacing between points
#binn the data points, get bin means, edges, and number 
bins = np.arange(0, 7, 0.5)#range and step size
bin_means, bin_edges, binnumber = stats.binned_statistic(x_sort[:,0], x_sort[:,1], statistic="mean", bins=nbins)
#print(bin_means)

#bin width
bin_width = bin_edges[1]-bin_edges[0];
#define empty arrays for x and y 
ix = []
iy = []
#use numberical method to calculate derivative
for i in range(1, nbins):
    ix.append(bin_edges[i] + bin_width/2.0)
    iy.append(bin_means[i])
    
#define empty arrays for derivatives 
ixd = []
iyd = []
#use numberical method to calculate noisy derivative
for j in range(2, len(ix)-2):
    ixd.append(ix[j])
    iyd.append((iy[j+1] - iy[j-1])/(ix[j+1] - ix[j-1]))
    
#arrays for five point method first derivative
ixpt = []
iypt = []

#for loop for five point method
for k in range(2*h, len(iy) - (2*h)):
    ixpt.append(ix[k])
    iypt.append((-(iy[k+2*h]) + 8*iy[k+h] - 8*iy[k-h] + iy[k-2*h])/(12*h*bin_width))
    
#simple second derivative    
ixsecond = []
iysecond = []   
for l in range(2, len(iyd)-2):
    ixsecond.append(ixd[l])
    iysecond.append((iyd[l+1] - iyd[l-1])/(ixd[l+1]-ixd[l-1]))
print(iysecond)
#five point stencil for second derviative
ixsecondpt = []
iysecondpt = []    
for m in range(2*h, len(iysecond) - (2*h)):
    ixsecondpt.append(ixsecond[m])
    iysecondpt.append((-(iysecond[m+2*h]) + 16*iysecond[m+h] - 30*iysecond[m] + 16*iysecond[m-h] - iysecond[m-2*h])/((12*h*h)*(bin_width)))

#plot commands
fig, ax = plt.subplots(1, 1, figsize=(6,4))
#second deriv plots
#ax.plot(ixsecond, iysecond)
#ax.plot(ixsecondpt, iysecondpt)
#plt.show()
#first deriv plots
ax.plot(ixpt, iypt, color="b", label="5 point method applied")
#ax.plot(ixd, iyd, color="orange", label="First Derivative")
plt.plot(x_values, y_values, "g.", label="Raw data", zorder=1)
plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], color="purple", lw=5, label="Binned data", zorder=2)
plt.legend()
plt.show()










