from collections import Counter


# Function to check if a number is a permutation of other
# it takes two strings as parameters, both being the respective numbers
def is_perm(n, x):
    if len(n) != len(x):
        return False
    else:
        a = sorted(n)
        b = sorted(x)
        for i in range(len(n)):
            if a[i] != b[i]:
                return False
        return True


# used counter dict to keep count of the number of cubic permutation of each number
cubes = Counter([a for a in range(1, 10000)])
i = 3
while True:
    for j in range(2, i):
        if is_perm(str(i ** 3), str(j ** 3)):
            cubes[j] += 1
            break
    i += 1
    if cubes.most_common()[0][1] == 5:
        print(cubes.most_common()[0][0]**3)
        break


