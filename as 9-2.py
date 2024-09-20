# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:39:20 2024

@author: limju
"""

#as9-2
import numpy as np

a = np.random.rand(10)

print(f'a = {a}')

string =  f"최댓값 : {a.max()}"\
          f"최솟값 : {a.min()}"\
          f"평균값 : {a.mean()}"
               
print(string)

#fin