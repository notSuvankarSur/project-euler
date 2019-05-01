def is_pallindrome(n):
    start = 0
    end = len(n) - 1

    while end > start:
        if n[start] == n[end]:
            start += 1
            end -= 1
        else:
            return False

    return True


def find_binary(n):
    b = ""
    if n == 1:
        return "1"
    if n % 2 == 0:
        b += find_binary(n // 2)
        b += "0"
    else:
        b += find_binary(n // 2)
        b += "1"
    return b


summ = 0
for i in range(1, 1000000, 2):
    if is_pallindrome(str(i)) and is_pallindrome(find_binary(i)):
        summ += i
        print(i)

print(summ)
