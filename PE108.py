from sympy import factorint
# 1/x + 1/y = 1/n
# let x = n + a, y = n + b, since x, y > 0, so x, y > n
# solving we get n**2 = a*b


def no_of_solutions(n):
    number = 1
    factors = factorint(n)
    for key, value in dict.items(factors):
        number *= (2 * value + 1)
    return (number + 1) // 2


num = 4
while 1:
    if no_of_solutions(num) > 1000:
        print(num, no_of_solutions(num))
        break
    else:
        num += 1
