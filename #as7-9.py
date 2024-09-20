#as7-9
#(1)
n_list1 = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
print('최댓값 : ', max(n_list1))
print('최솟값 : ', min(n_list1))

#(2)
n_list2 = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
def my_max(numbers):
    n_max = numbers[0]
    for n in numbers:
        if n_max < n:
            n_max = n
    return n_max
def my_min(numbers):
    n_min = numbers[0]
    for n in numbers:
        if n_min > n:
            n_min = n
    return n_min

print('최댓값 : ', my_max(n_list2))
print('최솟값 : ', my_min(n_list2))       

#(3)
n_list3 = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
from functools import reduce

n_max = reduce(lambda x,y: x if x>y else y, n_list3)
n_min = reduce(lambda x,y: x if x<y else y, n_list3)

print('최댓값 : ', n_max)
print('최솟값 : ', n_min)      

