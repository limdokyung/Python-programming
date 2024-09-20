#as7-7(1)
#(1)
n_list1 = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]
new_list1 = []

for n in n_list1:
    if n%12 == 0:
        new_list1.append(n)
print(n_list1)
print(new_list1)
#(2)
n_list2 = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]
new_list2 = []

for n in filter(lambda x: x%12 == 0, n_list2):
    new_list2.append(n)
print(n_list2)
print(new_list2)