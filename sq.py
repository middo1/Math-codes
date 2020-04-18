import math

for x in range(0,1000):
    for y in range(0,1000):
        s = math.sqrt(x**2 + y**2) 
        if s%1 == int() and x+y+s == 1000:
            print(x, y, s) 