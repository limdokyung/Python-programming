#as7-8
#(1)
n_list1 = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
new_list1 = []

for n in n_list1:
    if n>0:
        new_list1.append(int(n))

print(new_list1)

#(2)
n_list2 = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
new_list2 = []

for n in filter(lambda x: x>0, n_list2):
    new_list2.append(n)
new_list2 = list(map(int, new_list2))

print(new_list2)