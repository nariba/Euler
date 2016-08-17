#!/usr/local/bin/python3

import math

def sum_digit(n):
    l = []
    for i in range(len(str(n))):
        l.append(str(n)[i])
    s = 0
    for i in l:
        s += int(i)
    return s

if __name__ == '__main__':
    num = math.factorial(100)
    l = sum_digit(num)
    print(l)
