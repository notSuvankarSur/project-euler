champernownes_constant = "."
counter = 0
i = 1
while 1:
    if counter > 1000000:
        break
    champernownes_constant += str(i)
    for j in str(i):
        counter += 1
    i += 1
product = 1

for i in range(7):
    product *= int(champernownes_constant[10 ** i])

print(product)
