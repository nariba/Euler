#!/usr/local/bin/python3

import math

if __name__ == '__main__':
    l = []
    n = pow(2, 1000)
    for i in range(len(str(n))):
        l.append(str(n)[i])
    print(l)
    s = 0
    for i in l:
        s += int(i)
    print(s)
