n = int(input('enter the number: '))
i = 2
is_prime = True

while i < n:
    if n % i == 0:
        is_prime = False
    break
 i += 1

print( "is prime?" , is_prime)



