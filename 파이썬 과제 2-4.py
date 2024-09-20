# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:48:32 2024

@author: limju
"""

n = int(input('숫자를 입력하시오 : '))

prime=0

for i in range(2,n):
    if n%i==0:
        prime=0
        break
    else :
        prime=1

if prime==1:
    print(n,'은 소수입니다.')
else :
    print(n,'은 소수가 아닙니다.')
