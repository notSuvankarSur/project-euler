import time

fptr = open("path.txt")
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
mem = []

start = time.perf_counter()
for i in range(path_length):
    mem.append([])
# print(mem)
for i in range(path_length):
    mem[path_length - 1].insert(i, int(paths[path_length - 1][i]))
for i in range(path_length - 2, -1, -1):
    for j in range(0, i + 1):
        maximum = int(paths[i][j]) + max(mem[i + 1][j], mem[i + 1][j + 1])
        mem[i].insert(j, maximum)

end = time.perf_counter()
print(mem[0])

print(f"{end - start} s")
