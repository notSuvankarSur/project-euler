# odd period square roots
# used wiki link : https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
# contains a beautiful algorithm, good explanation and also a way to find the period
# refer link for more details
import math

count = 0
for number in range(2, 10001):
    contd_fract = []
    period = 0
    if math.sqrt(number) == int(math.sqrt(number)):
        continue
    a0 = math.floor(math.sqrt(number))
    contd_fract.append(a0)
    m = 0
    d = 1
    a = a0
    while a != 2 * a0:
        m = d * a - m
        d = (number - m ** 2) // d
        a = math.floor((a0 + m) / d)
        period += 1
        contd_fract.append(a)
    print(number, contd_fract)
    if period % 2 != 0:
        count += 1

print(count)
