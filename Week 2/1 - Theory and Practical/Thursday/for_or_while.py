""" Example where Either Loop Could be Used: """

# === Example 1: Sum of Numbers ===
# -- for loop option --
numbers = [1, 2, 3, 4, 5]
sum_result = 0

for num in numbers:
    sum_result += num

print(f"The sum is: {sum_result}")

# -- while loop option --
numbers = [1, 2, 3, 4, 5]
sum_result = 0
index = 0

while index < len(numbers):
    sum_result += numbers[index]
    index += 1

print(f"The sum is: {sum_result}")


# !!! For above, the for loop option will manage the indexing for you

# === Example 2: Finding the Maximum Element in a List ===
# -- for loop option --
numbers = [3, 8, 1, 6, 4, 2]

max_number = numbers[0]  # Assume the first element is the maximum

for num in numbers:
    if num > max_number:
        max_number = num

print(f"The maximum number is: {max_number}")

# -- while loop option --
numbers = [3, 8, 1, 6, 4, 2]

max_number = numbers[0]  # Assume the first element is the maximum
index = 1

while index < len(numbers):
    if numbers[index] > max_number:
        max_number = numbers[index]
    index += 1

print(f"The maximum number is: {max_number}")

# === Example 3: Sum of Squares ===
# -- for loop option --
numbers = [1, 2, 3, 4, 5]

sum_of_squares = 0

for num in numbers:
    sum_of_squares += num ** 2

print(f"The sum of squares is: {sum_of_squares}")

# -- while loop option --
numbers = [1, 2, 3, 4, 5]

sum_of_squares = 0
index = 0

while index < len(numbers):
    sum_of_squares += numbers[index] ** 2
    index += 1

print(f"The sum of squares is: {sum_of_squares}")

# -- Learner Question: Why i = 10 does not brake the loop?
# Create stability and one-purpose assignment by using a new variable if you \
# would like to use the temporary my_int variable after the loop execusion.
for my_int in range(1, 4):      # This line will keep overwriting my_int = 10
    print(my_int)
    my_int = 10
    print(my_int)
    my_external_int = my_int

print(my_external_int)

# Slicing example. Try for range, ie. for my_int in range(1, 4, 2):
my_string = "The sum of squares is"
my_new_string = my_string[17:10:-1]  # parameters to print "squares" in reverse
print(f">{my_new_string}<")

# === Example 4: User Input Validation
# -- while loop option --
user_input = input("Enter a positive integer: ")

# --- See below to test for a number without an error return
while not user_input.isdigit() or int(user_input) <= 0:
    print("Invalid input. Please enter a positive integer.")
    user_input = input("Enter a positive integer: ")

# At this point, user_input is a valid positive integer
print(f"You entered: {user_input}")

# NOTE: Bonus: Above is example of why casting can be seperate from input()

# -- for loop option --
# For loop inefficient example
for my_int in range(1, 10000):
    if user_input.isdigit() or int(user_input) > 0:
        break
    else:
        user_input = input("Enter a positive integer: ")