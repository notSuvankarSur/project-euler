import itertools


integers = []
for i in range(10):
    integers.append(i)
perm = list(itertools.permutations(integers))


def is_substr_div(number):
    prime = [2, 3, 5, 7, 11, 13, 17]  # only the primes required for dividing
    index = 0
    integer = 1
    while integer < len(number) - 2:
        num_str = ""
        num_str += number[integer] + number[integer + 1] + number[integer + 2]
        if int(num_str) % prime[index] == 0:
            integer += 1
            index += 1
            del num_str
        else:
            return False
    return True


def find_num(t):
    # converts a tuple into a number since we get tuples from permutation
    numb = ""
    for i in range(len(t)):
        numb += str(t[i])
    return numb


def total_substr_div():
    total = 0
    for pandigital in perm:
        x = find_num(pandigital)
        if is_substr_div(x):
            print(x)
            total += int(x)

    print(total)


if __name__ == "__main__":
    total_substr_div()
