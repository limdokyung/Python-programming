# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:34:05 2024

@author: limju
"""

for n in range(100,1000):
    hund=(n//100)
    ten = (n-(hund*100))//10
    one = n-(hund*100)-ten*10
    armstrong_sum = hund**3 + ten**3 + one**3
    
    if armstrong_sum == n:
        print(n,end=' ')
        