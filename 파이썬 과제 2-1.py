# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:38:30 2024

@author: limju
"""
integer=int(input('정수를 입력하시오 : '))
if integer%2==0:
    print(integer,'는 2로 나누어집니다.')
else :
    print(integer,'는 2로 나누어지지 않습니다.')
if integer%3==0:
    print(integer,'는 3으로 나누어집니다.')
else :
    print(integer,'는 3으로 나누어지지 않습니다.')
if integer%2==0 and integer%3==0:
    print(integer,'는 2와 3으로 나누어집니다.')
else :
    print(integer,'는 2와 3 모두로 나누어지지 않습니다.')