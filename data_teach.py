# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 11:28:04 2026

@author: lidar
"""

import random as rnd
import matplotlib.pyplot as plt
# create a 2d problem
n_classes = 2
n_inputs = 100      # overall
n_inputs_class = 50 # per class
#seed   = [[0,0]]*n_classes
inputs = [[0,0]]*n_inputs
teach  = [0]    *n_inputs # aka GT
#colors = ['#1f77b4', '#ff7f0e']
var = 0.6
for i in range(n_classes):
#    seed[i] = [rnd.random(), rnd.random()]
    seed = [rnd.random(), rnd.random()]
    for j in range(n_inputs_class):
        inputs[i*n_inputs_class+j] = [seed[0]+rnd.random()*var, seed[1]+rnd.random()*var]
        teach[i*n_inputs_class+j] = i # +1 due to plt.color
x = [];y=[]
for i in range(100):
    x.append(inputs[i][0])
    y.append(inputs[i][1])
#plt.scatter(x,y,'.',c=[colors[i] for i in teach])
plt.scatter(x,y,c=teach)