r = int(input("r = "))
n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))

def sum(r, n, a, b):
    for r in range(r, n + 1):
        c = 0
        s = a * r - b
        c += s
        if r == n:
            print(c)

sum(r, n, a, b) 