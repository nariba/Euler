#!/usr/local/bin/python3

import rabinMiller

def prime_factorization(number):
    table = []
    i = 2
    while i != 1 and number >= i:
        if rabinMiller.isPrime(i) and number % i == 0:
            table.append(i)
            number = number / i
        else:
            i += 1
    return table

def divisor_factor(number):
    table = []
    for i in range(1, number, 1):
        if number % i == 0:
            table.append(i)
    return table

if __name__ == '__main__':
    total = 0
    for a in range(2, 10000, 1):
        #print(a)
        l_a = divisor_factor(a)
        b = 0
        for j in l_a:
            b += int(j)
        if b != a:
            l_b = divisor_factor(b)
            a2 = 0
            for k in l_b:
                a2 += int(k)
            if a2 == a:
                print(str(a2) + 'is amicable numbers')
                total += a2
    print(total)
