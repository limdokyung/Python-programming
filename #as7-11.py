#as7-11
#(1)
words1 =['one', 'two', 'three', 'four']
new_words1 = []
for n in words1:
    new_words1.append(n[0].upper() + n[1:])
print(new_words1)

#(2)
words2 =['one', 'two', 'three', 'four']
new_words2 = list(map(lambda x: x[0].upper() + x[1:], words2))
print(new_words2)

