# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:45:11 2024

@author: limju
"""

n=int(input('숫자를 입력하세요 : '))
s=0

for i in range(n):
    s+= ((i+1)**2)
    
print('결과는',s,'입니다.')