# Program to identify Mines in code.

user_grid = [
    ["-", "-", "#", "-", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "#"]
]

# Program will iterate through grid and increment values that are next to Mine
# 
"""
[1, 2, '#', 2, '#']
[1, '#', 3, 3, 1]
[2, 4, '#', 2, 0]
[1, '#', '#', 3, 1]
[1, 2, 2, 2, '#']
"""

# get length of the Grid
grid_length = len(user_grid)
hash_count = 0

# created new list with values to be updated
new_list = [[0 for col in range(grid_length)] for row in range(grid_length)]

print(new_list)

# create a nested for-loop to iterate over user_grid and update values in new grid
# if at mine position in code, skip mine and add it to exact position in new list
# first conditional body will check if mine above, below, left and right
# second conditional body will check if mine top-right, top-left, bottom-right and bottom-left
# based of condition add 1 to current grid position in new grid. 

# if row > 0 and user_grid[row - 1][col] == "#"
#        new_list[row][col] += 1