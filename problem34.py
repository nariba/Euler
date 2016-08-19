#!/usr/local/bin/python3

import math

def factorial(num):
    value = 1
    for i in range(num, 0, -1):
        value *= i
    return value

if __name__ == '__main__':
    t = 0
    f_n = factorial(9)
    n = 9
    i = 1
    # calculate the limit
    while f_n > n:
        f_n = factorial(9)*i
        n = math.pow(10, i)-1
        i += 1

    # search curious number
    for num in range(f_n):
        s = 0
        for i in str(num):
            s += factorial(int(i))
            if s == num and s != 1 and s != 2:
                print(str(s) + ' is curious number.')
                t += s
    print(t)
