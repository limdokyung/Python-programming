# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:04:13 2024

@author: limju
"""

#as9-7
import numpy as np

#(1)
n = int(input('n을 입력하시오 : '))

matrix = np.eye(n, dtype = 'int32') 

for i in range(matrix.shape[0]):
    for j in range(i):
        matrix[i,j] = 1
        
print(matrix)

#(2)
s = matrix.mean() * matrix.size

print('행렬의 모든 원소의 합: ', s)

#(3)
row_sum = matrix.sum(axis=0)
print('행렬의 행 방향 성분의 합', row_sum)

#(4)
col_sum = matrix.sum(axis=1)
print('행렬의 열 방향 성분의 합', col_sum)

#fin








    
    