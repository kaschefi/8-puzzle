import copy
import heapq
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

def next_move(frontier):
    """Select and return the node with the smallest f(n) = g + h."""
    _, g, puzzle = heapq.heappop(frontier)
    return puzzle, g

def solve_puzzle(puzzle, heuristic):
    start = puzzle_to_tuple(puzzle)
    goal = (0, 1, 2, 3, 4, 5, 6, 7,8)

    frontier = []
    heapq.heappush(frontier, (heuristic(puzzle), 0, puzzle))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current, g = next_move(frontier)
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
                priority = new_cost + heuristic(next_state)
                heapq.heappush(frontier, (priority, new_cost, next_state))
                came_from[next_tuple] = current_tuple

    print("No solution found.")
    return []