from random import random


def generate_puzzle():
    puzzle = list(range(9))
    random.shuffle(puzzle)
    if not is_solvable(puzzle):
        return generate_puzzle()
    return puzzle

def is_solvable(puzzle):
    inversions = 0
    temp = [num for num in puzzle if num != 0]  # ignore blank
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] > temp[j]:
                inversions += 1
    return inversions % 2 == 0
