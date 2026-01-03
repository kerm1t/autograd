# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 11:21:24 2026

@author: lidar
"""


# loop over all input points
#    - multiply with weigths
#    - calculate cost

class neuron:
#    weights
#    bias (activation or delta ist/soll)
#    input
    def __init__(self, weights, bias):
        self.n = len(weights) 
        self.weight = weights
        self.bias = bias

    def process(self, item):
        z = 0
        for i in range(self.n):
            z += item[i]*self.weight[i]
        return (z+self.bias > 0)
    
    
#class perceptron:
def tester():
    n = neuron([1,2],1.5)


n = neuron(weights=[1,2],bias=1.5)
classe = n.process([1.1,4])
