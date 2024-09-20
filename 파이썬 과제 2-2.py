# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:43:49 2024

@author: limju
"""

r=5
x, y = input('x와 y를 입력하시오 : ').split(',')
x=int(x)
y=int(y)

distance = (x*x+y*y)**(1/2)

if distance<=r:
    print('원의 내부에 있음')
else:
    print('원의 외부에 있음')