#as8-8
#(1)
myl1 = [loop**3 for loop in range(11)]
print(myl1)

#(2)
myl2 = [loop**3 for loop in range(11) if loop%2 == 0]
print(myl2)

#(3)
myl3 = [loop**3 for loop in range(21) if loop%3 == 0 if loop%4 ==0]
print(myl3)

#(4)
myl4 = [loop**3 if loop % 2 == 0 else loop**2 for loop in range(11)]
print(myl4)

#(5)
myl5 = [a*b for a in range(4,6) for b in range(3,5)]
print(myl5)

#(6)
mys6 = {loop**3 for loop in range(11)}
print(mys6)

#(7)
mys7 = {loop**3 for loop in range(11) if loop % 2 == 0}
print(mys7)

#(8)
mys8 = {loop**3 for loop in range(21) if loop % 3 == 0 if loop % 4 == 0}
print(mys8)

#(9)
mys9 = {loop**3 if loop % 2 == 0 else loop**2 for loop in range(11)}
print(mys9)

#(10)
cube_dict10 = {mynum : mynum**3 for mynum in range(1,6)}
print(cube_dict10)
#(11)
cube_dict11 = {mynum : mynum**3 for mynum in range(1,6) if mynum%2 == 0}
print(cube_dict11)
#(12)
cube_dict12 = {mynum : mynum**3 for mynum in range(1,21) if mynum%2 == 0 if mynum%3 == 0}
print(cube_dict12)
#(13)
mydict_age = {'김': 31, '이': 32, '박': 40, '최': 50}
cube_dict13 = {mynum : 'old' if mydict_age[mynum] > 35 else 'young' for mynum in mydict_age}
print(cube_dict13)

#fin