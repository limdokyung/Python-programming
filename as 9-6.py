# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:58:22 2024

@author: limju
"""
#as 9-6
import numpy as np

x1 = np.array([[10, 20, 40, 60], [10, 20, 40, 40]])

dict_x = {}

rows = x1.shape[0]  
cols = x1.shape[1]  


for i in range(rows):
    for j in range(cols):
        if x1[i, j] not in dict_x:
            dict_x[x1[i, j]] = 1
        else:
            dict_x[x1[i, j]] += 1


print('x1 : ', x1)
for key in sorted(dict_x):  
    print(f'{key} : {dict_x[key]}번')
    

x2 = np.array([[80, 120, 40], [60, 80, 120], [40, 40, 40]])

dict_x = {}

rows = x2.shape[0]  
cols = x2.shape[1]  


for i in range(rows):
    for j in range(cols):
        if x2[i, j] not in dict_x:
            dict_x[x2[i, j]] = 1
        else:
            dict_x[x2[i, j]] += 1


print('x2 : ', x2)
for key in sorted(dict_x):  
    print(f'{key} : {dict_x[key]}번')
    
#fin
#객체지향으로 짜면 더 좋겠지만 다음에 해보도록 하겠습니다..