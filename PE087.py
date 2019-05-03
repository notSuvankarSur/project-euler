import sympy

list_two = list(sympy.sieve.primerange(1, 5e7 ** (1 / 2)))
list_three = list(sympy.sieve.primerange(1, 5e7 ** (1 / 3)))
list_four = list(sympy.sieve.primerange(1, 5e7 ** (1 / 4)))
prime_sum = set()
for i in list_four:
    for j in list_three:
        for k in list_two:
            total = k ** 2 + j ** 3 + i ** 4
            if total < 5e7:
                # print(k, j, i)
                prime_sum.add(total)

print(len(prime_sum))
