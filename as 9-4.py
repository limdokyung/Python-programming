# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:05:56 2024

@author: limju
"""

#as9-4

import numpy as np

n = int(input('n을 입력하시오 : '))

matrix = np.eye(n)

for i in range(n):
    
    matrix[i,i] *= i
    
print(matrix)

#fin