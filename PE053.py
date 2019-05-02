from math import factorial


def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


counter = 0
for i in range(2, 101):
    for j in range(0, i + 1):
        if comb(i, j) > 1e6:
            counter += 1

print(counter)
