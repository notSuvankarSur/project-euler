fptr = open("grid.txt")
x = fptr.read().split('\n')
grid = []
for i in x:
    inner = i.split(' ')
    grid.append(inner)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = int(grid[i][j])

print(grid)
maximum = 0
product = 1

for i in range(len(grid)):
    for j in range(len(grid[i])):
        product_one = 1
        product_two = 1
        product_three = 1
        product_four = 1
        for k in range(4):
            try:
                product_one *= grid[i][j + k]
                if product_one == 0:
                    break
            except IndexError:
                break

        for k in range(4):
            try:
                product_two *= grid[i + k][j]
                if product_two == 0:
                    break
            except IndexError:
                break

        for k in range(4):
            try:
                product_three *= grid[i + k][j + k]
                if product_three == 0:
                    break
            except IndexError:
                break

        for k in range(4):
            try:
                product_four *= grid[i + k][j - k]
                if product_four == 0:
                    break
            except IndexError:
                break

        product = max(product_one, product_two, product_three, product_four)
        if product > maximum:
            maximum = product

print(maximum)
