import math

# this equation is actually called Pell's equation
# wiki : https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents
# please refer to the link to understand my algorithm and learn more about convergents
# used the same algorithm to generate continued fractions as in problem 64
max_n = 0
dio = 0
for number in range(2, 1001):
    if math.sqrt(number) == int(math.sqrt(number)):
        continue
    a0 = math.floor(math.sqrt(number))
    m = 0
    d = 1
    a = a0

    numer = a0
    den = 1
    numer1 = 1
    den1 = 0

    while numer**2 - number * (den ** 2) != 1:
        m = d * a - m
        d = (number - m ** 2) // d
        a = math.floor((a0 + m) / d)

        numer2 = numer1
        numer1 = numer
        den2 = den1
        den1 = den

        numer = a * numer1 + numer2
        den = a * den1 + den2

    if numer > max_n:
        max_n = numer
        dio = number

print(dio, max_n)





