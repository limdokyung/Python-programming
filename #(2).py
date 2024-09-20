#(2)

f = open('random_numbers.txt','r')
s = f.read()
f2 = open('random_even.txt','w')

for _ in range(10):
    if f.readline()%2 == 0:
        f2.write(f.readline())

f2.close()

print(f2)