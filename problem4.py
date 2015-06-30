#!/usr/local/bin/python3.4

digit = []



for i in range(1, 1000):
    for j in range(1, 1000):
        product = i * j
        digit.append(product/10.0)

digit.pop(3)

print(digit)
