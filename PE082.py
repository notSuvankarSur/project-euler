"""
DP solution, first checked the top and right, and then compared that with the bottom,
the top row is compared with only the right and bottom, and the bottom row with top and right,
so we already have the optimal answer for the bottom row, using which we can get the others as well
Code by: Suvankar Sur
"""

with open('p081_matrix.txt') as fptr:
    mat = [[digit for digit in line.split()] for line in fptr]

path = []
for x in range(len(mat)):
    row = []
    for i in mat[x]:
        row = i.split(",")
        for j in range(len(row)):
            row[j] = int(row[j])
        path.append(row)

size = len(path)
# dp stores the minimum value from a column to the rightmost one
# so for the last column, the values of that column would be the values of dp as well, base case
dp = [path[i][size - 1] for i in range(size)]

for col in range(size - 2, -1, -1):

    for idx in range(size):
        if idx == 0:
            dp[idx] += path[idx][col]
        # checking up and right
        dp[idx] = min(dp[idx - 1] + path[idx][col], dp[idx] + path[idx][col])

    for idx in range(size - 2, -1, -1):
        # checking below
        # since we've calculated dp[idx] once we only need to compare it with the below path
        dp[idx] = min(dp[idx + 1] + path[idx][col], dp[idx])


print(dp)
print(min(dp))
