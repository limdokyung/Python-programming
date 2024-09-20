#(3)

f = open('random_numbers.txt','r')
s = f.read()
f3 = open('random_odd.txt','w')

for _ in range(10):
    if f.readline()%2 != 0:
        f3.write(f.readline())

f3.close()

print(f3)