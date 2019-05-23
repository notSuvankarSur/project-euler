"""
if the denominations were discrete(non-continuous), then we use an array, containing the possible numbers
since here the numbers are continuous, so I didn't use any array, to save space
I have used array in the next solution
Reference : GeeksForGeeks
"""


def number_of_ways(total):
    dp = [0 for _ in range(total + 1)]
    dp[0] = 1

    for i in range(1, total):
        for j in range(i, total + 1):
            dp[j] += dp[j - i]

    return dp[total]


print(number_of_ways(100))

