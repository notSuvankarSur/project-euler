"""
used the below dynamic programming algorithm at first, but it takes forever to solve this
"""


def number_of_ways(total):
    dp = [0 for _ in range(total + 1)]
    dp[0] = 1

    for i in range(1, total + 1):
        print(i)
        for j in range(i, total + 1):
            dp[j] += dp[j - i]

    return dp[total]


"""
Euler's pentagonal theorem to find the number of partitions
"""
# reference : online encyclopedia of integer sequences and Wiki on euler's pentagonal theorem and partitions
# generated the triangular numbers first, from there we can generate the generalized pentagonal numbers
triangular = [(i * (i + 1)) // 2 for i in range(1, 50000)]
pentagonal = []
# generating the generalized pentagonal numbers
for number in triangular:
    if number % 3 == 0:
        pentagonal.append(number // 3)

n = 1
partitions = [1]
while 1:
    sign = 0
    term = 0
    partitions.append(0)
    for idx in pentagonal:
        if idx > n:
            break
        # the sign changes for every 2 numbers
        if term % 4 > 1:
            sign = -1
        else:
            sign = 1
        partitions[n] += sign * partitions[n - idx]
        term += 1
    if partitions[n] % 1000000 == 0:
        print(n)
        break
    n += 1
