count = 0
for i in range(2):
    for j in range(3):
        for k in range(5):
            for l in range(11):
                for m in range(21):
                    for n in range(41):
                        for o in range(101):
                            x = 200 - (200 * i + 100 * j + 50 * k + 20 * l + 10 * m + 5 * n + 2 * o)
                            if x > 0 or x == 0:
                                print(i, j, k, l, m, n, o, x)
                                count += 1

print(count)


def number_of_ways(arr, total):

    dp = [0 for _ in range(total + 1)]
    dp[0] = 1

    for i in range(len(arr)):
        for j in range(arr[i], total + 1):
            dp[j] += dp[j - arr[i]]

    return dp[total]


array = [1, 2, 5, 10, 20, 50, 100, 200]
print(number_of_ways(array, 200))
