import numpy as np


hola = np.array([[1,2,3],[4,5,6],[7,8,9]])
hola1 = np.array([[1,2,3],[4,5,6]])

print(hola1)

print(hola*hola1)
print(hola@hola1)


class matlib(object):
    def __init__(self):
        pass
    
    def Add(self, matrix1, matrix2):
        result = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return result
    
    def Substract(self, matrix1, matrix2):
        result = [[matrix1[i][j] - matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return result
          
    def Product(self, matrix1, matrix2):
        result = [[matrix1[i][j] * matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return result
        
    def Division(self, matrix1, matrix2):
        result = [[matrix1[i][j] * matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return result
    
    def dot(self, vector1, vector2):
        result = 0
        for i in range(len(vector1)):
            result = result + vector1[i]*vector2[i]
        return result
    
    def cross(self, vector1, vector2):
        result = [vector1[1]*vector2[2] - vector1[2]*vector2[1],
                    vector1[2]*vector2[0] - vector1[0]*vector2[2],
                    vector1[0]*vector2[1] - vector1[1]*vector2[0]]
        return result
    
    def matmul(self,matrix1,matrix2):
        rows1 = len(matrix1)
        columns1 = len(matrix1[0])
        
        rows2 = len(matrix2)
        columns2 = len(matrix2[0])
        
        result = []
        
        #n1 x m1
        #n2 x m2
        if columns1 == rows2:
            for i in range(rows1):
                result.append([])
                for j in range(columns2):
                    result[i].append(0)
        
            for i in range(len(matrix1)):
       # iterate through columns of Y
                for j in range(len(matrix2[0])):
                    # iterate through rows of Y
                    for k in range(len(matrix2)):
                        result[i][j] += matrix1[i][k] * matrix1[k][j]
                    
            return result
        