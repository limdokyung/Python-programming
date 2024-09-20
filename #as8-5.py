#as8-5
#(1)
new_list = []
for x in range(1,100):
    if x%6 == 0:
        if x%7 == 0:
            new_list.append(x)
print(new_list)

#(2)
new_list2 = list(filter(lambda x: x%6 == 0 and x%7 == 0, range(1,100)))
print(new_list2)

#(3)
new_list3 = [x for x in range(1,100) if x%6 == 0 and x%7 == 0]
print(new_list3)

#fin