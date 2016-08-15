#!/usr/local/bin/python3

import math

def tri_num(n):
    return int(n*(n+1)/2)

def tri_num2(n):
    x = 0
    for i in range(n):
        x += i+1
    return x

def fac_num(n):
    num = 0
    for i in range(int(math.sqrt(n))-1):
        if n % (i+1) == 0:
            num += 1

    num = num * 2
    if int(math.sqrt(n)) == math.sqrt(n):
        num += 1
    return num

def fac_num2(n):
    num = 0
    for i in range(n):
        if n % (i+1) == 0:
            num += 1
    return num


if __name__ == '__main__':
    i = 1
    while True:
        tri = tri_num(i)
        fac = fac_num(tri)
        #print(i, tri, fac)
        if fac > 500:
            print(tri)
            break
        else:
            i += 1
