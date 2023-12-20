""" Open Class demo examples """

# === for loop variable declaration ===
# note below that my_var is underlined because it is not declared
# if iter_var:
#     pass

""" note below that my_var is not underlined because the for loop declared
    the variable my_var and controls the value of the variable
""" 
# for my_iter in range(0, 6):
#     print(f"for my_iter: {my_iter}")
#     my_iter = 10
#     print(f"set my_iter: {my_iter}")

# print(f"\nexit my_iter: {my_iter}\n")

# # If we want to use my_iter value then better to copy it into new variable
# for my_iter in range(0, 6):
#     print(f"for my_iter: {my_iter}")
#     if my_iter == 5:
#         iter_copy = my_iter
#         print(f"set my_iter: {iter_copy}")

# print(f"\nexit my_iter: {iter_copy}\n")

"""FOR LOOPS"""

# -- Format 1: Print numbers from 1 to 5
# for iter in range(1, 6):
#     print(f"format 1: {iter}\n")

# print()

# # Sting Example: my_strings = "This is my sentence"
# fruits = ['apple', 'banana', 'cherry']
# for iter_as_index in range(0, len(fruits)):
#     print(fruits[iter_as_index])

# -- Format 2: Iterate over elements in a list
# print()
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(f"format 2: {fruit}")

#0 - fruit = "apple"
#0 - fruit = "banana"
#0 - fruit = "cherry"
    
# Format 3: Iterate over elements while tracking iteration (enumerate)
print("my print")
fruits = ['apple', 'banana', 'cherry']
for fruit_iter, fruit in enumerate(fruits, start = 11):
    print(f"format 3: {fruit_iter}: {fruit}")
    
# if only 1 variable, both return values is placed in 1 variable as tuple
# print("my print")
# fruits = ['apple', 'banana', 'cherry']
# for fruit in enumerate(fruits, start = 1):
#     print(f"format 3: {fruit}")

