#as7-12
#(1)
fruits = {'Apple':'사과', 'Strawberry':'딸기', 'Peach':'복숭아', 'Grape':'포도'}
new_fruits = []
for key, value in fruits.items():
    fruit_string = key + "=" + value
    new_fruits.append(fruit_string)
print(new_fruits)

#2
new_fruits2 = list(map(lambda key: key + "=" + fruits[key], fruits))
print(new_fruits2)