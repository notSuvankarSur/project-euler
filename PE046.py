import math


def sieve_of_eratosthenes(n):
    a = []
    for i in range(0, n + 1):
        a.append(True)

    for i in range(2, int(math.sqrt(n)) + 1):
        j = i * i
        while j <= n:
            a[j] = False
            j = j + i

    prime_list = []
    for i in range(2, n + 1):
        if a[i]:
            prime_list.append(i)

    return prime_list


primes = sieve_of_eratosthenes(100000)
# print(x)
odd = []

for item in range(3, 100000):
    if item % 2 != 0:
        odd.append(item)

odd_composite = list(set(odd) - set(primes))
# print(z)

number = 0
for item in odd_composite:
    for prime in primes:
        for sq_num in range(1, 100000):
            if prime < item and item > 2 * sq_num * sq_num:
                number = prime + 2 * sq_num * sq_num
                if number > item:
                    break
                if number == item:
                    break
            else:
                break
        if number == item:
            break
    if number != item:
        print(item)
        break
