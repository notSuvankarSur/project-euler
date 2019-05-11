total = 0
for i in range(1001):
    if i % 10 == 0:
        total += 0
    else:
        total += i ** i % 10 ** 10

print(total % 10 ** 10)
