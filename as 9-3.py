# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:38:38 2024

@author: limju
"""

#as 9-3

import numpy as np

n = int(input('n을 입력하시오 : '))

matrix = np.zeros((n,n))

matrix[::2, ::2] = 1
matrix[1::2, 1::2] = 1

print(matrix)

#fin