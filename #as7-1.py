#as7-1
class Counter:
    def __init__(self, number = 0):
        if 0 <= number < 100:
            self.__number = number
        else: self.__number = 0
    
    def reset(self):
        self.__number = 0

    def inc(self):
        if self.__number < 100:
            self.__number += 1

    def dec(self):
        if self.__number > -1:
            self.__number -= 1

    def __str__(self):
        return f"C({self.__number})"
    
    def __add__(self, other):
        if not isinstance(other, Counter):
            raise TypeError("addition is supported only between Counter instances")
        elif self.__number > 100:
            self.__number = 0
        elif other.__number > 100:
            other.__number = 0
        else:
            new_value = self.__number + other.__number
        return Counter(new_value)
    
    def __sub__(self, other):
        if not isinstance(other, Counter):
            raise TypeError("Subtraction is supported only between Counter instances")
        elif self.__number < 0:
            self.__number = 0
        elif other.__number < 0:
            other.__number = 0
        else:
            new_value = self.__number - other.__number
        return Counter(new_value)
    
def main():
    c1 = Counter(10)
    c1.inc()
    print('c1 =', c1)
    c2 = Counter()
    c2.inc()
    c2.inc()
    c2.dec()
    print('c2 =', c2)
    c2.reset()
    print('c2 = ', c2)
    #9.9
    c1 = Counter(10)
    c2 = Counter(20)
    c3 = c1 + c2
    c4 = c1 - c2
    print('c3 = ', c3)
    print('c4 = ', c4)
main()
#c4의 결과가 음수면 __init__함수를 -10이 아닌 0으로 초기화 되야하는거 아닌가요??#



