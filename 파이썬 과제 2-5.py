# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:55:17 2024

@author: limju
"""
for i in range(2,13):
    prime = 1
    for j in range(2,i):
        if i%j == 0:
            prime=0
            break
      
    if prime==1:
        print('{} : 소수'.format(i))
    else :
        print('{} : 합성수'.format(i))