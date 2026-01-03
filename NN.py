# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 08:52:39 2026

@author: lidar
"""

from data_teach import create_data
from perceptron import neuron
import matplotlib.pyplot as plt

resi = create_data()
x = resi[0]
y = resi[1]
n = neuron([0.4,1.2],bias=0.7)
num = len(resi[0])
z = [0]*num
for i in range(num):
    z[i] = n.process([x[i],y[i]])
    
plt.scatter(x,y,c=z)