import math
import time

exponents = []

with open('p099_exponents.txt') as fptr:
    exp = fptr.read().split('\n')

#   exp contains list of strings, each string containing a combo of base and exponent pair
#   so this for loop is to convert the list into a 2D list, where each inner list contains a base-exp pair
for item in exp:
    temp = item.split(',')
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    exponents.append(temp)

#   instead of calculating the big integer, which would take a lot of time, I used logarithms,
#   as we know log(x**y) = y * log(x)

start = time.perf_counter()
maximum = 0
max_value = 0
for item in range(len(exponents)):
    if exponents[item][1] * math.log10(exponents[item][0]) > max_value:
        maximum = item + 1
        max_value = exponents[item][1] * math.log10(exponents[item][0])

end = time.perf_counter()
print(maximum)
print(f"{end - start} s")
