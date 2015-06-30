#!/usr/local/bin/python3.4

import math, rabinMiller

def prime_decomposition(num):
    for n in range(2, int(math.sqrt(num))):
        if num % n == 0 and rabinMiller.isPrime(n) ==True:
            print (n)

num = 600851475143
            
prime_decomposition(num)
