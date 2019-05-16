"""
This is the better version of PE018, it's basically the same problem
with larger input size, even here dp is used,
but here I traced the route through which shortest path is achieved
"""

fptr = open("max_path2.txt")
list_of_lengths = fptr.read().splitlines()
paths = [[]]
k = 0
for i in list_of_lengths:
    a = i.split(" ")
    paths.append(a)

paths.remove([])
path_length = len(paths)
# print(paths)
del list_of_lengths

route = []
for i in range(path_length):
    route.append([])

for i in range(path_length):
    route[i].append(int(paths[path_length - 1][i]))

for i in range(path_length - 2, -1, -1):
    for j in range(0, i + 1):
        if int(paths[i][j]) + sum(route[j]) > int(paths[i][j]) + sum(route[j + 1]):
            route[j].append(int(paths[i][j]))
        else:
            route[j] = route[j + 1][:]
            route[j].append(int(paths[i][j]))

route_actual = route[0]
del route

# print(route)

route_actual.reverse()
print(route_actual)

print(sum(route_actual))
