# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:48:23 2024

@author: limju
"""
n=int(input('정수를 입력하시오 : '))
n=str(n)

reverse_n = ''

for i in str(n):
    reverse_n = i + reverse_n

if reverse_n==n:
    print(n,'은(는) 거꾸로 정수입니다')
else :
    print(n,'은(는) 거꾸로 정수가 아닙니다.')