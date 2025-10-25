from astar import *

def calculate_manhattan_value(puzzle):
    # Input: puzzle
    # output: manhattan value
    # Function: it goes throw puzzle and calculate value base on manhattan distance
    value = 0
    for i in range(3):
        for j in range(3):
            temp = puzzle[i][j]
            if temp != 0:
                goal_row, goal_col = divmod(temp, 3)
                #divmod is a method that divides the number and returns the quotient and remainder
                # the result is the same as (a // b, a % b)
                # you can find the reason of using this formula in README.md under manhattan Distance
                value += abs(goal_row - i) + abs(goal_col - j)
    return value

def solve_with_manhattan(puzzle):
    # Input: unsolved puzzle
    # output: solved puzzle
    # Function: calls function solve_puzzle from class astar and send the puzzle and manhattan value to it
    return solve_puzzle(puzzle, calculate_manhattan_value)

def calculate_hamming_value(puzzle):
    goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    p = puzzle_to_tuple(puzzle)
    return sum(1 for i, v in enumerate(p) if v != 0 and v != goal[i])

def solve_with_hamming(puzzle):
    return solve_puzzle(puzzle, calculate_hamming_value)


