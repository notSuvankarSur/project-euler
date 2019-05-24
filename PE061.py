"""
Backtracking solution, could've used array instead of dict, but was trying a different approach using nested loops
then modified the algorithm, my first time writing backtracking, so..
can solve using nested loops as well, but the code wouldn't be neat
Code by : Suvankar Sur
"""

import math


def check_dict(d):
    """
    used to check the first and last numbers, if they are cyclic as well,
    it is important, as we can get many more answers without checking this
    :param d: answer dictionary
    """
    i = 1
    first = last = 0
    for v in dict.values(d):
        if i == 1:
            first = v
        if i == 6:
            last = v
        i += 1
    if first // 100 == last % 100:
        return True
    else:
        return False


def is_triangular(x):
    n = (math.sqrt(8 * x + 1) - 1) / 2
    if n == int(n):
        return True
    else:
        return False


def is_square(x):
    n = math.sqrt(x)
    if n == int(n):
        return True
    else:
        return False


def is_pentagonal(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    if n == int(n):
        return True
    else:
        return False


def is_hexagonal(x):
    n = (math.sqrt(8 * x + 1) + 1) / 4
    if n == int(n):
        return True
    else:
        return False


def is_heptagonal(x):
    n = (math.sqrt(40 * x + 9) + 3) / 10
    if n == int(n):
        return True
    else:
        return False


def is_octagonal(x):
    n = (math.sqrt(3 * x + 1) + 1) / 3
    if n == int(n):
        return True
    else:
        return False


def type_of_num(x):
    # checking for hexagonal first, as all hexagonal numbers are also triangular
    n = (math.sqrt(8 * x + 1) + 1) / 4
    if n == int(n):
        return 6
    n = (math.sqrt(8 * x + 1) - 1) / 2
    if n == int(n):
        return 3
    n = math.sqrt(x)
    if n == int(n):
        return 4
    n = (math.sqrt(24 * x + 1) + 1) / 6
    if n == int(n):
        return 5
    n = (math.sqrt(40 * x + 9) + 3) / 10
    if n == int(n):
        return 7
    n = (math.sqrt(3 * x + 1) + 1) / 3
    if n == int(n):
        return 8


nums = []
for num in range(1000, 10000):
    if is_triangular(num) or is_square(num) or is_pentagonal(num) or is_hexagonal(num) or is_heptagonal(num) or \
            is_octagonal(num):
        nums.append(num)

answer = {}


def check_num(number):
    if number not in dict.values(answer) and type_of_num(number) not in dict.keys(answer):
        return True
    return False


def generate(curr):
    """
    main backtracking algorithm, curr is the current number we need to check if it fits the solution
    """
    if len(answer) == 6 and check_dict(answer):
        return True
    if len(answer) == 0:
        answer[type_of_num(curr)] = curr
    if (curr % 100) * 100 < 1000:
        # if the next number to be generated is less than 4 digits, we return false
        return False
    for index in range((curr % 100) * 100, ((curr % 100) * 100) + 100):
        if index not in nums:
            continue
        if check_num(index):
            curr = index
            answer[type_of_num(curr)] = curr
            if generate(curr):
                return True
            # backtracking
            answer.pop(type_of_num(curr))
    return False


for num in nums:

    if generate(num):
        print(answer)
        break
    else:
        answer.clear()

total = 0

for val in dict.values(answer):
    total += val

print(total)
