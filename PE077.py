import sympy


def number_of_ways(arr, total):

    dp = [0 for _ in range(total + 1)]
    dp[0] = 1

    for i in range(len(arr)):
        for j in range(arr[i], total + 1):
            dp[j] += dp[j - arr[i]]

    return dp[total]


primes = list(sympy.sieve.primerange(1, 100000))
array = []
n = 10
for idx in primes:
    if idx >= 10:
        break
    array.append(idx)
while 1:
    if number_of_ways(array, n) > 5000:
        break
    n += 1
    array.clear()
    for idx in primes:
        if idx >= n:
            break
        array.append(idx)


print(n)
print(number_of_ways(array, n))