# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:47:13 2024

@author: limju
"""

r=10
x, y = input('x와 y를 입력하시오 : ').split(',')
x=int(x)
y=int(y)

distance = ((x-3)**2+(y-4)**2)**(1/2)

if distance<=r:
    print('원의 내부에 있음')
else:
    print('원의 외부에 있음')