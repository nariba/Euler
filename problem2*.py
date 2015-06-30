#!/usr/local/bin/python3.4

Fibonacci = [1, 2]
num = 400000

while True:
    if Fibonacci[ len(Fibonacci) - 1 ] \
       + Fibonacci[ len(Fibonacci) - 2 ] > num :
        break
    
    Fibonacci.append( Fibonacci[len(Fibonacci) - 1] \
                      + Fibonacci[len(Fibonacci) - 2] )

print( Fibonacci )
print( "", len(Fibonacci) )
print( "Max ( <", num, ") =", Fibonacci[len(Fibonacci) - 1] )

sum = 0
for i in range( 0, len(Fibonacci) - 1 ) :
    if Fibonacci[i] % 2 == 0 :
        sum += Fibonacci[i]

print("sum =", sum )
