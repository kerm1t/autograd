# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 15:30:22 2026

@author: lidar
"""

from matrix import Mat

# linear combination
# Y*a=b

# y^k -> n-by-d matrix, i.e. the input values, 2D-points or -features
# a^t -> e.g. (1,x1,x2) with weights x1, x2
# b_k -> arbitrarily specified constants

class LMS:
    def __init__(self):
# weights
        self.a = Mat([[5],[2]]) # arbitrary init
#        self.a = Mat([[5,2]]) # quick hack, should be a^t (transposed)
# bias(es?)
        self.b = Mat([[1],[1]]) # arbitrary margins
        self.theta = 1      # learn-end-criterion
        self.nu = 1         # any positive konstant
#        self.k = 0
    
    def train(self,y):
        k = 0
        tmp = 9999
        # do while error above learn-end-criterion
        print(f"k={k}, nu={self.nu}, a={self.a}, b={self.b}, y={y[k]}, tmp={tmp}, theta={self.theta}")
        while tmp > self.theta:
            k = k+1
            print(f"k={k}, nu={self.nu}, a={self.a}, b={self.b}, y={y[k]}, tmp={tmp}, theta={self.theta}")
            y_k = Mat(y[k])
            # nu/k is getting smaller with every k-step
            tmp = self.nu/k*y_k.matmul(self.b - self.a.matmul(y_k))
            
            # update weights now
            self.a = self.a + tmp
        return self.a
        