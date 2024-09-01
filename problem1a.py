import math
num = 15.329
a = math.ceil(num)
b = math.floor(num)
c = round(num)
print(a)
print(b)
print(c)
print(type(round(num)))
print(format(num, '.2f'))
print(type(format(num)))

avg = (a + b + c) / 3
print(" The average value of floor(), ceil() and round() is: ", avg)