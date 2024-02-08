# import math

# x=8.652
# print(math.ceil(x))
# print(math.floor(x))

# import math as m
# print(m.floor(10.58))

# from math import ceil, floor
# print(ceil(9.45))

# import random

# print(random.random())

# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)

# print(mylist)

# v1=random.random()
# v2=random.randint(0,100)
# print(v1,v2)

# nombres= ['Arturo','Julio','Dani','Aurora','Roberto','Martina']
# print(random.choice(nombres))

import math as m

x=15.6547

# print(m.ceil(x))
# print(m.floor(x))

# print(m.pow(4,3))
# print(m.gcd(6,9))
# print(m.factorial(4))

# print(m.e)
# print(m.pi)
from statistics import median

notas= [2 , 6, 7, 3, 7, 8, 6]
sumas = 0
for i in notas:
    sumas = sumas + i
#print(f"La media es {sumas/len(notas)}")
print(median(notas))





