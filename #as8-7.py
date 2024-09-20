#as8-7
#(1)
new_list1 = []
def flatten1(numbers):
    for sublist in numbers:
        for item in sublist:
            new_list1.append(item)
    return new_list1

org_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print('org_list =', org_list)
print('new_list =', flatten1(org_list))

#(2)
def flatten2(numbers):
    new_list2 = [item for sublist in numbers for item in sublist]
    return new_list2

new_list2 = list(flatten2(org_list))
print('org_list = ', org_list)
print('new_list2 = ', new_list2)

#fin