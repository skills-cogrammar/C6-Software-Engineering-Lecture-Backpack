# Example 1 - Zero Division Error
# try:
#     first_num = int(input("Enter your first number: "))
#     second_num = int(input("Enter your second number: "))

#     results = first_num / second_num

#     print(f"The result of {first_num} divided by {second_num} is {results}")
# except ZeroDivisionError as e:
#     print(f"{e}: You can't divide by Zero!")

# Example 2 - ValueError
# while True:
#     try:
#         first_num = int(input("Enter your first number: "))
#         second_num = int(input("Enter your second number: "))

#         results = first_num + second_num

#         print(f"The result of {first_num} + {second_num} is {results}")
#         break
#     except ValueError as e:
#         print(f"{e}: Try to enter a numerical value")

# Example 3 - Index Error + Value Error

# list_of_numbers = [12, 23, 34, 45, 56]

# while len(list_of_numbers) > 0:
#     try:
#         user_index = int(input("Enter the position of the value you seek: "))
#         accessed_value = list_of_numbers[user_index]
#         print(f"The value at psotion {user_index} is {accessed_value}")
#     except IndexError as e:
#         print(f"{e}: The position you seek lies outside the range of the list")
#     except ValueError as e:
#         print(f"{e}: The value you have entered is not a integer value.")

# print("We skipped the loop")

# Example 4
# empty string validation 
# user_quote = input("Enter your most famous quote: ")

# if user_quote == "":
#     raise Exception("TRY TO TAKE THIS SERIOUSLY!")
# else:
#     print("Excellent stuff, this will go down in history! ")

# # x = "" # - false 
# # x = 0 # - false

# Example 5 - Use case of try/except over if/else
# try:
#     zero_float_value = "89.5"
#     one_float_value = "A Long Sentence"

#     print(f"Converted Value Zero: {float(zero_float_value)}")
#     print(f"Converted Value One: {float(one_float_value)}")
# except ValueError:
#     print("The value caught is not a string!")

# Example 6 - File handling
# try:
#     with open("list_cats.txt", "r") as file:
#         content = file.readlines()
#         print(f"File content: {content}")
# except FileNotFoundError:
#     print("The file is not in the current folder")

# file opening
# try:
#     file = open("list_cats.txt", "r")
#     content = file.readlines()
#     print(f"File content: {content}")
# except FileNotFoundError:
#     print("The file is not in the current folder")
# finally:
#     file.close()