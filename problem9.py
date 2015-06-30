#!/usr/local/bin/python3.4

import math

for a in range(1, 500):
    for b in range(1, 500):
        if a < b:
            c = 1000 - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                print(a * b * c)
