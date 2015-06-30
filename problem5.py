#!/usr/local/bin/python3.4

num = 10

product = 1

for i in range(1, num + 1):
    if product % i != 0:
        product *= i
    print(i, product)
