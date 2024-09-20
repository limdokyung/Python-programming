# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:02:10 2024

@author: limju
"""

#as9-8
import numpy as np

#(1)
a = np.array([ [2,1,1], [1,2,1], [1,1,2] ])
b = np.array([ [16], [9], [3] ])

x = np.linalg.solve(a,b)

print(f'x = {x[0,0]}, y = {x[1,0]}, z = {x[2,0]}')

#(2)
A = np.array([ [2, 1, 1], [1, 2, 1], [1, 1, 2] ])

det_A = np.linalg.det(A)

print('det(A) = ', int(round(det_A)))

#fin