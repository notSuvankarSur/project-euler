import numpy as np

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

path = np.array(path)
size = len(path)
dp = []
for i in range(size):
    dp.append([])
    for _ in range(size):
        dp[i].append(-1)

for i in reversed(range(80)):
    for j in reversed(range(80)):
        if i == 79 and j == 79:
            dp[i][j] = path[i][j]
        elif (i == 78 and j == 79) or (i == 79 and j == 78):
            dp[i][j] = path[i][j] + dp[79][79]
        elif i == 79:
            dp[i][j] = path[i][j] + dp[i][j + 1]
        elif j == 79:
            dp[i][j] = path[i][j] + dp[i + 1][j]
        else:
            dp[i][j] = min(path[i][j] + dp[i][j + 1], path[i][j] + dp[i + 1][j])

print(dp[0][0])
