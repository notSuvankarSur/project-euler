import sympy


def prime_factorisation(n):
    # returns a dict with keys as primes and values as their exponents
    return sympy.factorint(n)


maximum = 0
number = 0
limit = 1000000
ratio = 1
while limit >= 10:
    if sympy.isprime(limit):
        limit -= 1
        continue
    totient_value = 1
    prime_dict = prime_factorisation(limit)
    for key, value in prime_dict.items():
        if value == 1:
            totient_value *= key - 1
        else:
            totient_value *= key ** value - key ** (value - 1)
    ratio = limit / totient_value
    if ratio > maximum:
        maximum = ratio
        number = limit
    limit -= 1

print(maximum, number)
