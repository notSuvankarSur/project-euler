fptr = open("max_product.txt")
digits = []
for i in fptr.read():
    if i != '\n':
        digits.append(int(i))
# print(digits)
maximum = 0
for i in range(0, len(digits)):
    product = 1
    for j in range(0, 13):
        product *= digits[i + j]
        if product == 0:
            break
    if product > maximum:
        maximum = product

print(maximum)
