""" Tutorial Class Demo"""

# found_mikie = False

# while not found_mikie:
#     print("My friend's name is Andrew.")
#     your_friend = input("Provide your friend's name: ").lower()
#     if your_friend == "mikie":
#         found_mikie = True

# print(f"Loop is exited with friend {your_friend}.")

# === continue and break statements ===
# -- Without continue we will have to use below code

# 0 to 10, we only want 0 to 5 and 8 to 10
# for iteration in range(0, 6):   # Print 0 to 5
#     print(iteration)

# for iteration in range(8, 11):  # Print 8 to 10
#     print(iteration)

# print() # Open line between examples

# # -- Another alternative to replace continue statement
# for iteration in range(0, 11):   # Print 0 to 5 & 8 to 10
#     if iteration > 5 and iteration < 8:
#         pass
#     else:
#         print(iteration)

# print("\n--Exit the continue-alter for-loop\n")

# # -- Use continue as alternative to the above
# for iteration in range(0, 11):   # Print 0 to 5 & 8 to 10

#     if iteration > 5 and iteration < 8:
#         continue
#     print(iteration)

# print("\n--Exit the continue for-loop\n")

# -- Break statement in single for-loop
# for iteration in range(0, 11):   # Print 0 to 5 & 8 to 10
#     if iteration > 5 and iteration < 8:
#         break

#     print(iteration)

# if iteration > 5:
#     print("We will take a break soon!")

# -- Break statement in nested for-loop
# for first_iter in range(0, 3):
#     for inner_iter in range(0, 7):        # Print 0 to 5 & 8 to 10
#         if inner_iter > 5 and inner_iter < 8:
#             break                         # Only breaks out of inner_iter

#         print(f"{first_iter} : {inner_iter}")
#     print()

# print("\n--Exit the first_iter break for-loop\n")

# === Task 8 - Star pattern with for-loop ===

# -- According to the instructions the below is not allowed
# - 1st half pattern
# pattern_rows = 9
# for iter in range(1, pattern_rows/2):
#     pass #logic
"""
*
**
***
****
*****
"""
# # - 2nd half pattern
# for iter in range(pattern_rows/2 + 1, pattern_rows):
#     pass #logic

"""
****
***
**
*
"""

# This is what is required - Do your best to write dynamic code (not static)
# condition = True
# for iter in range(1, 10):
#     if condition:
#         pass #logic
#     else:
#         pass #logic

# pattern_width = input("How wide would you like the pattern: ")
# for iter in range(1, pattern_width * 2):
#     if condition:
#         pass #logic
#     else:
#         pass #logic

"""
*
**
***
****
*****
****
***
**
*
"""

# Remember: Concatenation => 'yes' + 'yes' + 'yes' = 'yesyesyes'
#           Multiplication => 'yes' * 3 = 'yesyesyes' 

# HINT, HINT, HINT
# print('yes' + 'yes' + 'yes')
# print('yes' * 3)

# === Task 7 - Repeat input until stop with while-loop ===
"""
ask the user to press enter or enter the word "stop"
while the user has not entered "stop"
    print "Hello"
    ask the user to press enter or enter the word "stop"
"""
# user_input = input("Please press enter or enter the word 'stop': ")

# while user_input.lower() != "stop":
#     print("Hello")
#     user_input = input("Please press enter or enter the word 'stop': ")

# print()

# # --- Multiple input example for flight destinations

# user_input = input("Please press enter or enter the word 'stop': ")

# while user_input.title() not in ["London", "Amsterdam", "Frankfurt"]:
#     print("Hello")
#     user_input = input("Please press enter or enter the word 'stop': ")

# # --- Multiple input example for valid full name

# full_name = input("Enter your full name: ")
# # full_name = "Luke Dunne"

# valid_name = False
# while not valid_name:
#     if ' ' not in full_name:
#         full_name = input("Please re-enter your full name: ")
#     else:
#         valid_name = True

# === Simple for-loop example that might not be so simple ===
# -- Option 1
print(" ======= To the Power Examples =======\n")

base = 2
power = 5
result = base
# 2 ^^ 5 => 2 * 2 * 2 * 2 * 2
for iter in range(power-1):
    result = result * base

print(f"power result: {result}\n")

# -- Option 2
base = 2
power = 5
result = base
# 2 ^^ 5 => 2 * 2 * 2 * 2 * 2
for iter in range(2, power + 1):
    result = result * base    # 1st iteration is base * base (power of 2)

print(f"power result: {result}\n")

# -- Option 3
# -- Let's have a look at another example that makes logical sense. --
base = 2
power = 5         # base * base * base * base * base => for power == 5
result = 1        # start with result == 1
# 2 ^^ 5 => 2 * 2 * 2 * 2 * 2
for iter in range(1, power + 1):      # The start changes from 2 to 1.
    result = result * base    # 1st iteration is 1 * base (power of 1)

print(f"power result: {result}\n")

# --- Algorithm short code
# result = result * base 
# result *= base 