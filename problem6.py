#!/usr/local/bin/python3.4

num = 100

SumofSquares = 0
SquareofSums = 0

for i in range(1, num + 1):
    SumofSquares += i ** 2
    SquareofSums += i

SquareofSums = SquareofSums ** 2

print("the Square of the Sums =", SquareofSums)
print("the Sum of the Squares =", SumofSquares)
print('Difference =', SquareofSums - SumofSquares)
