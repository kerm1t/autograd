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
#            print(f"item[{i}]={item[i]} * weight[{i}]={self.weight[i]}")
            z += item[i]*self.weight[i]
        print(f"z={z} / n={self.n} + bias={self.bias} > 0 ?")
        print(f"result: {z/self.n + self.bias}")
        return (z/self.n+self.bias > 0)
    
    
#class perceptron:
def tester():
    n = neuron([1,2],1.5)


if __name__ == '__main__':
    n = neuron(weights=[1,2],bias=1.5)
    classe = n.process([1.1,4])
