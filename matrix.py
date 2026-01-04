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
    
    # instance method
    def matmul(self, b): # not commutative
        # print("Mat.matmul:")
        # self.pprint() # debug only
        # b.pprint()    # debug only
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
            
    def __sub__(self, b):
        # print("Mat.sub:")
        # self.pprint() # debug only
        # b.pprint()    # debug only
        # 2do: check if both matrices have same dimensions
        cols = len(self.rows[0])
        rows = len(self.rows)
        res = Mat.empty(rows,cols)
        for i in range(rows):
            for j in range(cols):
                res.rows[i][j] = self.rows[i][j] - b.rows[i][j]
        return res

    def __mul__(self, s):
        # print("Mat.mul w. scalar:")
        cols = len(self.rows[0])
        rows = len(self.rows)
        res = Mat.empty(rows,cols)
        for i in range(rows):
            for j in range(cols):
                res.rows[i][j] = self.rows[i][j]*s
        return res

    def __add__(self, b):
        # print("Mat.add:")
        # self.pprint() # debug only
        # b.pprint()    # debug only
        # 2do: check if both matrices have same dimensions
        cols = len(self.rows[0])
        rows = len(self.rows)
        res = Mat.empty(rows,cols)
        for i in range(rows):
            for j in range(cols):
                res.rows[i][j] = self.rows[i][j] + b.rows[i][j]
        return res

    # example
    # [1.0, 0.6] > [0.5,0.5] ? Yes
    # [1.0, 0.3] > [0.5,0.5] ? No
    def __gt__(self, b):
        print("Mat.gt_than:")
        self.pprint() # debug only
        b.pprint()    # debug only
        # 2do: check if both matrices have same dimensions
        cols = len(self.rows[0])
        rows = len(self.rows)
        res = True
        for i in range(rows):
            for j in range(cols):
                if (self.rows[i][j] < b.rows[i][j]):
                    res = False
        return res


if __name__ == '__main__':
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
    d = Mat([[-1,3],[0,2]])
    e = d-b
    e.pprint()
    
    
