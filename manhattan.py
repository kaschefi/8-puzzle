import heapq
from logic import *
import copy

def calculate_manhattan_value(puzzle):
    value = 0
    for i in range(3):
        for j in range(3):
            temp = puzzle[i][j]
            if temp != 0:
                goal_row, goal_col = divmod(temp, 3)
                value += abs(goal_row - i) + abs(goal_col - j)
    return value


def next_move(frontier, cost_so_far, came_from):
    """Select and return the node with the smallest f(n) = g + h."""
    _, g, puzzle = heapq.heappop(frontier)
    return puzzle, g


def solve_with_manhattan(puzzle):
    start = puzzle_to_tuple(puzzle)
    goal = (0, 1, 2, 3, 4, 5, 6, 7,8)

    frontier = []
    heapq.heappush(frontier, (calculate_manhattan_value(puzzle), 0, puzzle))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current, g = next_move(frontier, cost_so_far, came_from)
        current_tuple = puzzle_to_tuple(current)

        if current_tuple == goal:
            print("Solved!")
            # reconstruct path
            path = []
            while current_tuple is not None:
                # convert tuple back to 3x3 list
                path.append([list(current_tuple[i:i + 3]) for i in range(0, 9, 3)])
                current_tuple = came_from[current_tuple]
            path.reverse()
            return path  # return full path (list of puzzles)

        for move_name, next_state in possible_moves(current, came_from):
            next_tuple = puzzle_to_tuple(next_state)
            new_cost = cost_so_far[current_tuple] + 1

            if next_tuple not in cost_so_far or new_cost < cost_so_far[next_tuple]:
                cost_so_far[next_tuple] = new_cost
                priority = new_cost + calculate_manhattan_value(next_state)
                heapq.heappush(frontier, (priority, new_cost, next_state))
                came_from[next_tuple] = current_tuple

    print("No solution found.")
    return []