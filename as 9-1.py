# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:39:19 2024

@author: limju
"""
#as9-1

import numpy as np
#(1)
a = np.arange(1,11)
print(f'a = {a}')

#(2)
print(a[::-1])

#(3)
print(a[::-1].reshape(2,5))

#(4)
print(a[::-1].reshape(5,2))

#fin