#!/usr/bin/python3
import sys


def factorization(n):
    res = []
    prime = 2
    if n < 2: 
        return res
    while n > 1:
        if n % prime == 0:
            res.append(prime)
            n = int(n/prime)
        else:
            prime  += 1
    return res

print(factorization(int(sys.argv[1])))