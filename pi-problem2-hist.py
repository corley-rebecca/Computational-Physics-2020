#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 06:30:46 2021

@author: rebeccacorley
"""
#Computational Physics: 23-08-2021 Problem 1
'''
This code estimates the value of pi using Monte Carlo methods with additional edit:
    optimize code (if possible)
    generate plot to show pi becoming more accurate as statistics increase 
    Want two plots with different number of trials showing pi becoming more accurate 
'''

#python libraries used for this code
import numpy as np
import matplotlib.pyplot as plt
import random 
import statistics

#start_time = time.time() #start time to see how long code runs

'''
Consider a game of darts.
I want to set up two different experiments with different numbers of darts.
Experiment 1: 10000 darts thrown
'''
n_iterations = 100000 #define number of points in histogram
n_darts = 10000 #define number of darts thrown
circle = 0 #initialize circle counts
square = 0 #initialize square counts
hist_data = [] #initalize empty array for histogram 

#big loop
for i in range(n_iterations):
    
    circle = 0
    square = 0
    #random generator loop
    for j in range(n_darts):
        
        x = random.random() #normalized from (0,1) as floats
        y = random.random()
       
        if (((x*x) + (y*y)) <= (1.0)):
            circle += 1.0
            square += 1.0
        else:
            square += 1.0 
  
    hist_data.append(4*(float(circle)/float(square)))   
    

average = statistics.mean(hist_data)
stdev = statistics.stdev(hist_data)

plt.hist(hist_data, 50)
plt.vlines(np.pi, ymin=0, ymax=8000, linestyles="--", label="True pi", color="black")
plt.legend()
plt.ylabel('Probability')
plt.xlabel('Pi Extimate')
plt.show()

print("Average Value: " +str(average))
print("Standard Deviation: " +str(stdev))






