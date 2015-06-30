#!/usr/local/bin/python3.4

fibonacci = [1, 2]
sum = 2
n = 1
num = 4000000
while fibonacci[n-1] + fibonacci[n] < num:
    fibonacci.append(fibonacci[n-1] + fibonacci[n])
    print(fibonacci[n])
    if fibonacci[n+1] < num and fibonacci[n+1] % 2 == 0:
        sum += fibonacci[n+1]
    n += 1

print(fibonacci)
print('sum = ',sum)

