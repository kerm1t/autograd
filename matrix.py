# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 18:56:48 2026

@author: lidar
"""

class Mat:
    def __init__(self, rows):
        self.rows = rows

    @classmethod
    def empty(self, rows, cols):
        mat = []
        for i in range(rows):
            mat.append([0]*cols)
        return Mat(mat)
    
    def matmul(self, b): # not commutative
        global res
        colsA = len(self.rows[0])
        rowsB = len(b.rows)
        if (colsA == rowsB):
            rowsA = len(self.rows)
            colsB = len(b.rows[0])
            res = Mat.empty(rowsA,colsB)
            for i in range(rowsA):
                for j in range(colsB):
                    t = 0
                    for k in range(colsA):
                        t += self.rows[i][k]*b.rows[k][j]
                    res.rows[i][j] = t
            return res
        else:
            print("matmul : %dx%d cannot be multiplied with %dx%d"%(len(self.rows),colsA,rowsB,len(b.rows)))
    
    def pprint(self): # pretty print
        print(type(self).__name__)
        for i in range(len(self.rows)):
            print(self.rows[i])

a = [[1,2,3],
     [2,3,4]]
b = [[2,2],
     [3,3]]
# above matrixes can only be multiplied b*a, but not a*b
# number of cols of matrix 1 to be = number of rows of Matrix 2

a = Mat([[1,2,3],[2,3,4]]) # 2,3 Matrix
b = Mat([[2,2],[3,3]])
#a.pprint()
#b.pprint()

c = a.matmul(b) # not possible
c = b.matmul(a)

c.pprint()