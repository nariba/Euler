#!/usr/local/bin/python3.4

sum = 0

num = 1000

for i in range(0, num):
    if i % 3 == 0 or i % 5 == 0 :
        sum += i
        print(i, sum)

print(sum)
