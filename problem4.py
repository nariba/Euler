#!/usr/local/bin/python3.4

max_product = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if str(product) == str(product)[::-1]:
            if max_product < product:
                max_product = product

print(max_product)
