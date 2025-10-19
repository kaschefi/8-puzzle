from astar import *

def calculate_manhattan_value(puzzle):
    value = 0
    for i in range(3):
        for j in range(3):
            temp = puzzle[i][j]
            if temp != 0:
                goal_row, goal_col = divmod(temp, 3)
                value += abs(goal_row - i) + abs(goal_col - j)
    return value

def solve_with_manhattan(puzzle):
    return solve_puzzle(puzzle, calculate_manhattan_value)