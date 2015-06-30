#!/usr/local/bin/python3.4

import rabinMiller

num = 10001

primes = []
i = 1

while True:
    if rabinMiller.isPrime(i) == True:
        primes.append(i)
        if len(primes) == num :
            break
        
    i += 1

print(primes[num - 1])
