import math
import time


def nod(n):
    """calculates the number of divisors of a given number"""
    i = 1
    num = 0
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        num += 1

    while i < math.sqrt(n):
        if n % i == 0:
            num += 2
        i += 1
    return num


def triangular_num(x):
    return (x * (x + 1)) // 2


start = time.perf_counter()
k = 1
while nod(triangular_num(k)) <= 500:
    print(triangular_num(k), nod(triangular_num(k)))
    k += 1

end = time.perf_counter()
print(triangular_num(k))
print(end - start)