# sum of each column 

"""
example output:
    [
        [1, 2, 3],
        [12, 23, 34],
        [10, 20, 30]
    ]
sum = 23, 45, 67 

3 X 3
[
[] [] []
[] [] []
[] [] []
]
"""

# The code `num_rows = int(input("Enter the number of rows: "))` prompts the user to enter the number
# of rows they want in the grid and stores the input as an integer in the variable `num_rows`.
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

# The line `user_grid = [[0 for col in range(num_cols)] for row in range(num_rows)]` is creating a
# 2-dimensional list (or grid) with `num_rows` rows and `num_cols` columns. Each element in the grid
# is initialized to 0.
user_grid = [[0 for col in range(num_cols)] for row in range(num_rows)]

# print(user_grid)
# The code `print(user_grid)` is printing the entire grid, which is a 2-dimensional list, to display
# the initial values of all the elements in the grid.
# print(user_grid)

# The code `for x in user_grid: print(x)` is iterating over each row in the `user_grid` and printing
# the row. This is done to display the initial values of all the elements in the grid before the user
# inputs their own values.
# for x in user_grid:
#     print(x)

# This code snippet is responsible for taking user input to populate the grid with values.
for row in range(num_rows):
    print(f"\nRow value: {user_grid[row]}")
    print(f"Row No.{row + 1}")
    for col in range(num_cols):
        print(f"\nCol No.: {col + 1}")
        user_grid[row][col] = int(input("Enter a value: "))
    print(user_grid)

for x in user_grid:
    print(x)

sum_column = 0

# Calculate the sum of each column
for row in range(num_rows):
    for col in range(num_cols):
        print(f"{user_grid[col][row]}\n")
        sum_column += user_grid[col][row]
    print(f"The sum of column{row + 1} is: {sum_column}")
    sum_column = 0
