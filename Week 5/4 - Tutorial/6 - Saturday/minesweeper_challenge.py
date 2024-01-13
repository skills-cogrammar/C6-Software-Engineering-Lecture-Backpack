# The line `from tabulate import tabulate` is importing the `tabulate` function from the `tabulate`
# module. The `tabulate` function is used to format and display tabular data in a visually appealing
# way.
from tabulate import tabulate

# Program to identify Mines in code.

user_grid = [
    ["-", "-", "#", "-", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "#"]
]

# directional checks
# Never Eat Sour Worms
# North East South West

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
# List comprehension appraoch
new_list = [[0 for col in range(grid_length)] for row in range(grid_length)]

# Traditional Approach with nested loop
# new_list = []
# for row in range(grid_length):
#     row_list = []
#     new_list.append(row_list)
#     for col in range(grid_length):
#         row_list.append(0)
#     # print(new_list)

# print(new_list)



# create a nested for-loop to iterate over user_grid and update values in new grid
# if at mine position in code, skip mine and add it to exact position in new list
# first conditional body will check if mine above, below, left and right
# second conditional body will check if mine top-right, top-left, bottom-right and bottom-left
# based of condition add 1 to current grid position in new grid. 

# if row > 0 and user_grid[row - 1][col] == "#"
#        new_list[row][col] += 1


# [1, 2, '#', 2, '#']
# [1, '#', 3, 3, 1]
# [2, 4, '#', 2, 0]   ==> current test row
# [1, '#', '#', 3, 1]
# [1, 2, 2, 2, '#']


# num sequence 0 1 2 3 4 
for row in range(grid_length):
    for col in range(grid_length):

        # Skip "#" and add into new list
        if user_grid[row][col] == "#":
            new_list[row][col] = "#"
            continue
        
        
        # This code is checking if there is a mine above the current position in the user_grid. If
        # there is a mine, it increments the value in the corresponding position in the new_list by 1.
        if row > 0 and user_grid[row - 1][col] == "#":
            new_list[row][col] += 1

        
        # This code is checking if there is a mine below the current position in the user_grid. If
        # there is a mine, it increments the value in the corresponding position in the new_list by 1.
        if row < grid_length - 1 and user_grid[row + 1][col] == "#":
            new_list[row][col] += 1

        # This code is checking if there is a mine to the left of the current position in the
        # user_grid. If there is a mine, it increments the value in the corresponding position in the
        # new_list by 1.
        if col > 0 and user_grid[row][col - 1] == "#":
            new_list[row][col] += 1

        # This code is checking if there is a mine to the right of the current position in the
        # user_grid. If there is a mine, it increments the value in the corresponding position in the
        # new_list by 1.
        if col < grid_length - 1 and user_grid[row][col + 1] == "#":
            new_list[row][col] += 1

        """Second conditonal body NE, NW, SW, SE"""

        # This code is checking if there is a mine in the top-left position of the current position in
        # the user_grid. If there is a mine, it increments the value in the corresponding position in
        # the new_list by 1.
        if row > 0 and col > 0 and user_grid[row - 1][col - 1] == "#":
            new_list[row][col] += 1
      
        # This code is checking if there is a mine in the top-right position of the current position
        # in the user_grid. If there is a mine, it increments the value in the corresponding position
        # in the new_list by 1.
        if row > 0 and col < grid_length - 1 and user_grid[row - 1][col + 1] == "#":
            new_list[row][col] += 1

        # This code is checking if there is a mine in the bottom-left position of the current position
        # in the user_grid. If there is a mine, it increments the value in the corresponding position
        # in the new_list by 1.
        if row < grid_length - 1 and col > 0 and user_grid[row + 1][col - 1] == "#":
            new_list[row][col] += 1

        # This code is checking if there is a mine in the bottom-right position of the current
        # position in the user_grid. If there is a mine, it increments the value in the corresponding
        # position in the new_list by 1.
        if row < grid_length - 1 and col < grid_length - 1 and user_grid[row + 1][col + 1] == "#":
            new_list[row][col] += 1

# print(user_grid)   
# for grid in new_list:
#     print(grid)
# # print(new_list)

# Using tabulate method to improve data ouput 
# The code is using the `tabulate` function from the `tabulate` module to format and display the
# `user_grid` and `new_list` in a visually appealing way.
tab_user_grid_ouput = tabulate(user_grid, tablefmt='fancy_grid')
print("\nFirst List with Mines and Dashes below: ")
print(tab_user_grid_ouput)

print("Second List with values around Mines updated below: ")
tab_new_list_ouput = tabulate(new_list, tablefmt='fancy_grid')
print(tab_new_list_ouput)
