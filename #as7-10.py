#as7-10
#(1)
new_list1 = []
for n in range(1,100):
    if n%6 == 0:
        new_list1.append(n)
print(new_list1)
#(2)
new_list2 = []
for n in filter(lambda x: x%6 == 0, range(1,100)):
    new_list2.append(n)
print(new_list2)