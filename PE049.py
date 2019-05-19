import itertools
import math


def permuts(integers):
    integer_list = []
    for i in str(integers):
        integer_list.append(int(i))
    perms = list(set(itertools.permutations(integer_list)))
    actual = []
    for i in range(len(perms)):
        num_str = ""
        for j in range(len(perms[i])):
            num_str += str(perms[i][j])
        actual.append(int(num_str))
        del num_str
    actual.sort()
    return actual


a = []


def sieve_of_eratosthenes(n):
    for index in range(0, n + 1):
        a.append(True)

    for index in range(2, int(math.sqrt(n)) + 1):
        j = index * index
        while j <= n:
            a[j] = False
            j = j + index

    b = []
    for index in range(2, n + 1):
        if a[index]:
            b.append(index)

    return b


x = sieve_of_eratosthenes(10000)
y = sieve_of_eratosthenes(1400)
prime_list = list(set(x) - set(y))
prime_list.sort()
# print(prime_list)
count = 0
for i in range(len(prime_list) - 2):
    permutations = permuts(prime_list[i])
    start = permutations.index(prime_list[i])
    # while permutations[start] != prime_list[i]:
    #     start += 1
    difference = 0
    for j in range(start + 1, len(permutations)):
        if a[permutations[j]]:
            difference = permutations[j] - prime_list[i]
            if (prime_list[i] + 2 * difference) in permutations and a[prime_list[i] + 2 * difference]:
                print(prime_list[i], prime_list[i] + difference, prime_list[i] + 2 * difference)
                print(difference)
                count += 1
                break
    if count == 2:
        break
    del permutations, difference
