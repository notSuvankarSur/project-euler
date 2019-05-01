import sympy


# func to check if the number is front truncatable prime
def truncate_front(n):
    front = []
    for i in range(1, len(str(n))):
        front.append(int(str(n)[i:]))
    for i in front:
        if not sympy.isprime(i):
            return False
    return True


# func to check if the number is backwards truncatable prime
def truncate_back(n):
    back = []
    for i in range(len(str(n)) - 1, 0, -1):
        back.append(int(str(n)[:i]))
    for i in back:
        if not sympy.isprime(i):
            return False
    return True


trunc = []


# This method basically generates possible truncatable primes and returns them as a list to optimize the search time
# initialised ends with the possible numbers which can be at start or end with 2 as an exception
# similarly initialised mid with the respective possible digits

def gen_trunc():
    ends = [2, 3, 5, 7]
    mid = [1, 3, 7, 9]
    while ends:
        prime = ends.pop(0)
        # this checks for the front truncatable primes, and adds them to the ends list for possible ends
        for digit in mid:
            temp = prime * 10 + digit
            if sympy.isprime(temp):
                ends.append(temp)
                # if it is back truncatable as well, then we add it to temp as well
                if truncate_back(temp):
                    trunc.append(temp)
    return trunc


summ = 0

# Here we check temp list and get the actual 11 numbers
for i in gen_trunc():
    if truncate_front(i) and truncate_back(i):
        summ += i
        print(i)

print(summ)
