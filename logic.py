import random


def generate_puzzle():
    puzzle = list(range(9))
    puzzle_matrix = [[0 for i in range(3)] for j in range(3)]
    random.shuffle(puzzle)
    if not is_solvable(puzzle):
        return generate_puzzle()
    for i in range(9):
        puzzle_matrix[i // 3][i % 3] = puzzle[i]
    return puzzle_matrix

def is_solvable(puzzle):
    inversions = 0
    temp = [num for num in puzzle if num != 0]  # ignore blank
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] > temp[j]:
                inversions += 1
    return inversions % 2 == 0
