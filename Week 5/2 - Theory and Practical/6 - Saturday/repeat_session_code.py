# example 1

random_numbers = [
    [12, 23, 34],
    [1, 2, 3],
    [10, 20, 30]
]

# Accessing Element
# element = grid[row_index][column_index]
random_num_from_grid = random_numbers[2][1]
# print(random_num_from_grid)

# Iterating through 2D List
for item in random_numbers:
    print(item)
    for sub_item in item:
        print(sub_item)

# Common Operations

# sum of each row
total_sum_of_list = [sum(row) for row in random_numbers]
# print(total_sum_of_list)

# sum of all elements
total_sum = sum(total_sum_of_list)
# print(f"The total sum of all elements: {total_sum}")

# Appending Items to 2D List

# Append a row
random_numbers.append([11, 22, 33])

# Append to a column
for row in random_numbers:
    print(f"Current Row Items: {row}")
    row.append(int(input("Enter a number: ")))

print(random_numbers)

# Things to Look out for
"""
Index out of range ===> accessing items outside the list range or scope

jagged_list = [
    [1, 2],
    [2, 3],
    [4, 5]
]

# debugging tips
- Making use 'print' to debug code
- Exception handling through runtime error catching

"""

# Best Practices
"""
1. Utilize list comprehension - this is efficient and reduces bulk of code.
2. Remember Nested Loops - when working with 2D lists is to make use of 
nested loops.
3. Always Document - clearly document your 2D list as these can get complex.
"""

# Data science tools 
"""
Libraries that are used for 2D (3D, 4D ...) lists
- Numpy
- Pandas
"""
