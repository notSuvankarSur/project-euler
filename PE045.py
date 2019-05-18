import math
import time

"""
if a number is triangular, it is also hexagonal, so generating only the triangular
numbers, and checking if it is pentagonal as well.
"""


def is_hexa(x):
    n = (math.sqrt(8 * x + 1) + 1) / 4
    if n - int(n) == 0:
        return True
    else:
        return False


def is_penta(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    if n - int(n) == 0:
        return True
    else:
        return False


i = 144
start = time.perf_counter()
while 1:
    n = i * (2*i - 1)
    if is_penta(n):
        print(n)
        break
    i += 1

print(time.perf_counter() - start)

