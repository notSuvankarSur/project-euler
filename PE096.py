"""
Backtracking used. Reference : GeeksForGeeks
but their code has a small flaw in the used_in_block and is_safe methods
Code by : Suvankar Sur
"""


# finds an empty block, stores the row, col in list l
def find_empty_block(arr, l):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def used_in_row(arr, row, number):
    for i in range(len(arr)):
        if arr[row][i] == number:
            return True
    return False


def used_in_col(arr, col, number):
    for i in range(len(arr)):
        if arr[i][col] == number:
            return True
    return False


def used_in_block(arr, row, col, number):
    if row % 3 != 0:
        row -= row % 3
    if col % 3 != 0:
        col -= col % 3
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == number:
                return True
    return False


def check_current_is_safe(arr, row, col, number):
    return not used_in_row(arr, row, number) and not used_in_col(arr, col, number) and \
           not used_in_block(arr, row, col, number)


def solve(arr):
    rc = [0, 0]
    if not find_empty_block(arr, rc):
        return True

    row = rc[0]
    col = rc[1]

    for number in range(1, 10):
        if check_current_is_safe(arr, row, col, number):

            arr[row][col] = number
            if solve(arr):
                return True
            arr[row][col] = 0
    # backtracking
    return False


def main():
    """
    Extracting the data and inserting into a 3D list, puzzle is a list containing the puzzles,
    and each puzzle is another 9 x 9 2D list
    so puzzles dimensions are 50 x 9 x 9
    """
    puzzles = list(line.split() for line in open('p096_sudoku.txt'))
    i = 0
    new = []
    while i < 50:
        new += puzzles[10 * i + 1: 10 * i + 10]
        i += 1
    for idx in new:
        temp = idx[:]
        list.clear(idx)
        for j in temp[0]:
            idx.append(int(j))
    list.clear(puzzles)
    i = 0
    while i < 50:
        temp = new[9 * i: 9 * i + 9]
        puzzles.append(temp)
        i += 1

    total = 0
    for puzzle in puzzles:
        if solve(puzzle):
            total += int(str(puzzle[0][0]) + str(puzzle[0][1]) + str(puzzle[0][2]))
            print(int(str(puzzle[0][0]) + str(puzzle[0][1]) + str(puzzle[0][2])))

    print(total)


if __name__ == "__main__":
    main()
