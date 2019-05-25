"""
As you may have noticed the number of fractions possible for a given denominator is the value of its totient,
that is, the number of numbers less than n, which are co-prime to n
"""

import sympy


def prime_factorisation(n):
    return sympy.factorint(n)


total = 0
i = 1000000
while i >= 2:
    if sympy.isprime(i):
        total += i - 1
        i -= 1
        continue
    totient_value = 1
    prime_dict = prime_factorisation(i)
    for key, value in prime_dict.items():
        if value == 1:
            totient_value *= key - 1
        else:
            totient_value *= key ** value - key ** (value - 1)
    total += totient_value
    i -= 1

print(total)
