# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:20:48 2024

@author: limju
"""

#as9-9
import cmath

class Function:
    def __init__(self, func = None):
        self.func = func

    def value(self, x):
        if self.func:
            return self.func(x)

class Quadratic(Function):
    def __init__(self, a, b, c):
        super().__init__(lambda x: a * x**2 + b * x + c)
        self.a = a
        self.b = b
        self.c = c

    def get_roots(self):
        d = self.b**2 - 4 * self.a * self.c
        x1 = (-self.b + cmath.sqrt(d)) / (2 * self.a)
        x2 = (-self.b - cmath.sqrt(d)) / (2 * self.a)
        return (x1, x2)

def main():
    e = Quadratic(1, 5, 6)
    print('방정식의 해 : ', e.get_roots())  

main()