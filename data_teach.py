# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 11:28:04 2026

@author: lidar
"""

import random as rnd
import matplotlib.pyplot as plt

# create a 2d problem
# would be nice to have different disributions, e.g normal, rayleigh etc.
def create_data():
    n_classes = 2
    n_inputs = 100              # overall
    n_inputs_class = 50         # per class
    inputs = [[0,0]]*n_inputs
    teach  = [0]    *n_inputs   # aka GT
    var = 0.6
    for i in range(n_classes):
        seed = [rnd.random(), rnd.random()] # don't store seed
        for j in range(n_inputs_class):
            inputs[i*n_inputs_class+j] = [seed[0]+rnd.random()*var, seed[1]+rnd.random()*var]
            teach[i*n_inputs_class+j] = i
    x = [];y=[]
    for i in range(100):
        x.append(inputs[i][0])
        y.append(inputs[i][1])
    return (x,y,teach)

if __name__ == '__main__':
    res = create_data()
    x = res[0]
    y = res[1]
    teach = res[2]
    plt.scatter(x,y,c=teach)
