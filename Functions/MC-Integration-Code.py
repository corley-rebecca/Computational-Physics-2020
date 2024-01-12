#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:15:08 2021

@author: rebeccacorley
"""

import numpy as np
import matplotlib.pyplot as plt



data = np.genfromtxt('function_real.dat')
data2 = np.genfromtxt('function_unknown.dat')

plt.scatter([x[0] for x in data], [x[1] for  x in data], marker="*")
plt.show()
plt.scatter([x[0] for x in data2], [x[1] for  x in data2], marker=".", color="g")
plt.show()