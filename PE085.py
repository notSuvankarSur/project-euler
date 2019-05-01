i = j = 0
for i in range(2, 2000):
    for j in range(i + 1, 2000):
        num_of_rects = ((i * (i - 1)) // 2) * ((j * (j - 1)) // 2)
        if abs(2000000 - num_of_rects) <= 5:
            print(i, j)

print((i - 1)*(j - 1))
