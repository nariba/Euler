#!/usr/local/bin/python3.4

import rabinMiller

num = 2000000
prime_sum = 0

for i in range(1, num + 1):
    if rabinMiller.isPrime(i):
        prime_sum += i

print(prime_sum)
