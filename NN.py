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
n = neuron([0.4,1.2],bias=-0.8) # kinda works for some random distributions
num = len(resi[0])
z = [0]*num
for i in range(num):
    z[i] = n.process([x[i],y[i]])
    
plt.scatter(x,y,c=z)

# -----------------------------------------------
# above doesn't work, need a much simpler example
# -----------------------------------------------

# 1 discrimination: y = 0.7x + 1
# 1 input, class 1 or "true": x=1.2, y=1.7
# 1 input, class 0 or "false": x=1.6, y=0.7

# n = neuron([1,0.7],bias=-1.1)
# num = 2
# x = [0]*num;x[0]=1.2;x[1]=1.6
# y = [0]*num;y[0]=1.7;y[1]=0.7
# z = [0]*num
# for i in range(num):
#     z[i] = n.process([x[i],y[i]])
# plt.scatter(x,y,c=z)
