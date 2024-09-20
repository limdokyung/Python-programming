# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:27:03 2024

@author: limju
"""

#as9-10

class Animal:
    def __init__(self, age):
        self.age = age

    def eat(self):
        print("동물이 먹고 있습니다.")

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(age)
        self.name = name
        self.breed = breed

def get_oldest_cat(*cats):
    max_age = max(cat.age for cat in cats)
    print(f"가장 나이가 많은 고양이는 {max_age}살입니다.")
    
def main():
    a = Cat("야옹이", 2, "순종")
    b = Cat("나비", 3, "순종")
    c = Cat("냥냥", 5, "순종")

    get_oldest_cat(a, b, c)
    
main()
