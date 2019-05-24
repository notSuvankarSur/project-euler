import sympy

no_of_primes = 3
side_length = 2
corner = 9

while no_of_primes / (2 * side_length + 1) > 0.1:
    side_length += 2
    for i in range(3):
        corner += side_length
        if sympy.isprime(corner):
            no_of_primes += 1
    corner += side_length

print(side_length + 1)
