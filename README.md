# 8-puzzle
the goal of this project is to solve a 8-puzzle
using a* search where the h(x) is calculated 
with manhattan distance and hamming distance
to see the difference is speed and memory usage
# Structure
in astar.py is the a* search algorithm and also the
logic behind generating a solvable puzzle and possible 
movement in the game

in manhatten.py is the manhattan distance value 
calculation and calling the a* search algorithm to 
solve the puzzle with manhattan distance

in hamming.py is the hamming distance value calculation
and calling the a* search algorithm to solve the puzzle
with hamming distance

# Usage
to start the program run the main.py file 

# Manhattan Distance
in function calculate_manhattan_value we go throw the 
puzzle and calculate the manhattan distance for each 
tile and we do it using divmod method to get the 
remainder and the quotient, if you think about it 
the manhattan distance is the sum of the remainder
and the quotient minus current location ,lets say 8 is in place on 1 so 8/3 = 2
and 8%3 = 2 now -> 2 + 2 = 4 -> 4 - 1 + 1 = 4
where 1 is i and 0 is j 

# astar
## solvable
a puzzle is solvable when inversion is a even number 
An inversion occurs when a larger-numbered tile precedes a 
smaller-numbered tile in the puzzle’s linear (flattened) form
 ignoring the blank (0 or space).
example: 321 456 789 
inversion is 2
## solve_puzzle 
in here we use heapq which is a binary tree
for which every parent node has a value less
than or equal to any of its children.