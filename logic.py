import copy
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

def move_up(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                continue
            if i > 0 and puzzle[i - 1][j] == 0:
                puzzle[i][j], puzzle[i - 1][j] = puzzle[i - 1][j], puzzle[i][j]
                return puzzle
    return puzzle

def move_down(puzzle):
    for i in reversed(range(len(puzzle))):
        for j in reversed(range(len(puzzle[i]))):
            if puzzle[i][j] == 0:
                continue
            if i < 2 and puzzle[i + 1][j] == 0:
                puzzle[i][j], puzzle[i + 1][j] = puzzle[i + 1][j], puzzle[i][j]
                return puzzle
    return puzzle

def move_left(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                continue
            if j > 0 and puzzle[i][j - 1] == 0:
                puzzle[i][j], puzzle[i][j - 1] = puzzle[i][j - 1], puzzle[i][j]
                return puzzle
    return puzzle

def move_right(puzzle):
    for i in reversed(range(len(puzzle))):
        for j in reversed(range(len(puzzle[i]))):
            if puzzle[i][j] == 0:
                continue
            if j < 2 and puzzle[i][j + 1] == 0:
                puzzle[i][j], puzzle[i][j + 1] = puzzle[i][j + 1], puzzle[i][j]
                return puzzle
    return puzzle

def puzzle_to_tuple(puzzle):
    return tuple(num for row in puzzle for num in row)

def possible_moves(puzzle, visited):
    moves = []
    for move_func, name in [(move_up, "up"), (move_down, "down"),
                            (move_left, "left"), (move_right, "right")]:
        new_puzzle = move_func(copy.deepcopy(puzzle))
        t = puzzle_to_tuple(new_puzzle)
        if new_puzzle != puzzle and t not in visited:
            moves.append((name, new_puzzle))
    return moves