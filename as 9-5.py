# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:22:21 2024

@author: limju
"""

#as 9-5

import numpy as np

n = int(input('n을 입력하시오 : '))

a = np.ones((n,n), dtype = 'int32')
print('a 행렬\n', a)

a[1:n-1, 1:n-1] = 0
b = a
print('b 행렬\n', b)

#fin
