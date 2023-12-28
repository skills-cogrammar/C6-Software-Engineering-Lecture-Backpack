

# Syntax Error Examples: ####################################
# Make sure that variable names are differenciate and that a typing error does not lead to a logical error.
# 111 - Missing closing parenthesis
print("Hello, World!"

# 222 - Unclosed string
message = 'Hello, World!

# 333 - # Incorrect indentation
if True:
print("Condition is True")

# 444 - Missing colon after if statement
if True
    print("Condition is True")
	
# 555 - Invalid operator
result = 10 **/ 2

# 666 - Using reserved words as variable names
if = 5

# 777 - # Mismatched parentheses
result = (3 + 5 * (2 - 4)


# Runtime Error Examples:  ###################################
# 111 - Attempting to divide by zero
result = 10 / 0

# 222 - Accessing an index that is out of range
my_list = [1, 2, 3]
print(my_list[5])

# 333 - Performing an operation on incompatible data types
result = "5" + 3

# 444 - Attempting to open or access a file that does not exist
with open("nonexistent_file.txt", "r") as file:
    content = file.read()

# 555 - Passing an argument to a function with an invalid value
number = int("abc")

# 666 - Attempting to access an attribute or method that does not exist
my_list = [1, 2, 3]
my_list.upper()

my_string = "string"
my_string.upper()		# Note the colour of .upper() in your editor

# 777 - Accessing a key in a dictionary that does not exist
my_dict = {"a": 1, "b": 2}
value = my_dict["c"]

# 888 - Performing arithmetic that results in an overflow
result = 2 ** 1000000

# 999 - Attempting to import a module that does not exist
import nonexistent_module

# 000 - Running out of memory
my_large_list = [0] * 10**8
"""
when you execute my_large_list = [0] * 10**8, it creates a list with 100 million zeros. 
This can be useful for creating large lists with identical elements or initializing 
data structures with a specific pattern. 
This may lead to a MemoryError if the system does not have 
sufficient available memory to accommodate such a large list.
"""


# Logical Error Examples: #####################################

# 1111 -- Incorrect Formula Used --
# Incorrect formula for calculating the area of a circle (Incorrect formula)
import math

radius = 5
incorrect_area = 2 * math.pi * radius  
print(incorrect_area)

# ???? Circle Radius formala should be correct_area = math.pi * radius**2

# 2222 -- Error and Algorithmic Implementation --
#(Incorrect use of parentheses)

x = 10
y = 5

result = x - y * 2  
print(result)

# 3333 -- Incorrect conditional statement --
# or should be and
age = 25

if age >= 18 or age <= 21:
    print("Age is between 18 and 21.")

# 4444 -- Incorrect algorithm for finding the maximum element in a list --
# if all the values in numbers list are negative then max_number value would be 0 which is not in the list.
numbers = [3, 8, 2, 6, 1]

max_number = 0
for num in numbers:
    if num > max_number:
        max_number = num
print(max_number)



	# =========   A try-except block is used to catch and handle exceptions in Python. 
	try:
		# Code that might raise an exception
		numerator = int(input("Enter the numerator: "))
		denominator = int(input("Enter the denominator: "))
		
		result = numerator / denominator
		
		# This block will be skipped if an exception occurs
		print("Result:", result)

	except ValueError as ve:
		# Handle the case where the user enters a non-integer
		print(f"Error: {ve}. Please enter valid integers.")

	except ZeroDivisionError:
		# Handle the case where the user tries to divide by zero
		print("Error: Division by zero is not allowed.")

	except Exception as e:
		# Handle any other unexpected exceptions
		print(f"An unexpected error occurred: {e}")

	else:
		# This block will be executed if no exception occurs
		print("No exceptions were raised.")

	finally:
		# This block will be executed whether an exception occurred or not
		print("This block always executes, providing cleanup or finalization.")
