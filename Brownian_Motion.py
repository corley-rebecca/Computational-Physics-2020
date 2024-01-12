#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:20:42 2021

@author: rebeccacorley
"""
import numpy as np
import matplotlib.pyplot as plt 


repititions = 1000 # number of steps in each walk
final_r = [] # empty array for magnitude of steps in each walk
x_initial=0 # define initial position at 0
y_initial=0
walk=10



for i in range(repititions):
    x_initial = 0
    y_initial = 0
    for j in range(walk):
       #create a random walk in 2D (x,y) direction
       x = np.random.randn(repititions)
       y = np.random.randn(repititions) 
       if i %10==0: # If this iteration divided by 10 is 0, append value
           r = np.sqrt(x[i]**2 + y[i]**2)
           final_r.append(r)
    #average = r /len()
    
#plot the random walk
plt.plot(x,y)

print(final_r)
fig, ax = plt.subplots(1,1,figsize=(10,6))
ax.hist(final_r, bins=100)
plt.show()
