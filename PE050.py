import math
from bisect import bisect_left


def binary_search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


def sieve_of_eratosthenes(n):
    a = []
    for i in range(0, n + 1):
        a.append(True)

    for i in range(2, int(math.sqrt(n)) + 1):
        j = i * i
        while j <= n:
            a[j] = False
            j = j + i

    b = []
    for i in range(2, n + 1):
        if a[i]:
            b.append(i)

    return b


x = sieve_of_eratosthenes(1000000)
y = [0]
z = 0
no_of_primes = 0
length = len(x)
for i in range(0, length):
    y.append(z + x[i])
    z += x[i]
result = 0
for i in range(no_of_primes, len(y)):
    for j in range(i - (no_of_primes + 1), -1, -1):
        if y[i] - y[j] > 1000000:
            break
        if binary_search(x, y[i] - y[j]) >= 0:
            no_of_primes = i - j
            result = y[i] - y[j]

print(result)
print(no_of_primes)
