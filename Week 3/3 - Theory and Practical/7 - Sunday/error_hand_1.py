# Example 1
# user_input = int(input("Enter a number greater than 10: "))

# if user_input < 10:
#     raise Exception("You have entered a value less than 10!")

# Example 2
# user_input = input("Enter a number greater than 10: ")

# if not user_input.isdigit():
#     raise ValueError("You have entered an invalid input!")
# elif int(user_input) < 10:
#     raise ValueError("You have entered a value less than 10!")

# Example 3
# try:
#     user_input = int(input("Enter a number greater than 10: "))

#     if user_input < 10:
#         raise Exception("You have entered a value less than 10!")
# except ValueError:
#     print("Invalid value entered!")
