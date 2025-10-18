from logic import *
def calculate_manhattan_value(puzzle):
    value = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            temp = puzzle[i][j]
            if temp != 0:
                goal_row = temp // 3
                goal_col = temp % 3
                value += abs(goal_row - i) + abs(goal_col - j)
    return value


import copy


def next_move(puzzle, visited):
    moves = possible_moves(puzzle, visited)
    min_value = calculate_manhattan_value(puzzle)
    best_node = puzzle

    for move_name, new_puzzle in moves:
        temp_value = calculate_manhattan_value(new_puzzle)
        if temp_value < min_value:
            min_value = temp_value
            best_node = new_puzzle

    return best_node
def solve_with_manhattan(puzzle, max_steps=1000):
    visited = set()
    steps = 0

    while calculate_manhattan_value(puzzle) != 0 and steps < max_steps:
        visited.add(puzzle_to_tuple(puzzle))
        new_puzzle = next_move(puzzle, visited)
        if puzzle_to_tuple(new_puzzle) == puzzle_to_tuple(puzzle):
            print("stuck, no improvement")
            break
        puzzle = new_puzzle
        steps += 1

    return puzzle