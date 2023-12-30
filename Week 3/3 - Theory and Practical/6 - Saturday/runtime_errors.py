# Error 1

# ZeroDivisionError - division by zero
# num1 = 66
# num2 = 0

# result = num1 / num2

# print(result)

# String Example
# my_string = "Execute order 66"

# print(my_string[0:6])


# Error 2 - IndexError
#              0   1   2   3
# rando_list = [12, 34, 45, 56]
# # # print(rando_list[3])      

# Correct Code
# for num in (0, 4)
# for num in range(1, len(rando_list)):
#     print(num)
#     # print(rando_list[num])

# # Incorrect Code - IndexError recreation
# for num in range(5):
#     print(num)
#     # print(rando_list[num])


# Error 3 - TypeError 
#              0   1   2   3
# rando_list = [12, 34, 45, 56]
# # print(rando_list[3])      

# Correct Code
# # for num in (0, 4)
# for num in range(1, len(rando_list)):
#     print(num)
#     # print(rando_list[num])

# Incorrect Type Error Recreation
# for num in (0, 4)
# for num in len(rando_list):
#     print(num)
    # print(rando_list[num])

# num1 = 19
# my_bestest_friend = "Barney the dinasour"

# result = num1 + my_bestest_friend
# print(result)

# Error 4 - NameError
# print(f"{my_bestest_friend} is a prehistoric purple being of light and love who is cuddly.")

# (0, 1, 2, 3)
# for value in range(4):
#     print(value)

# print(f"Current result of this variable is: {value}")

# Value Errors
# the value we have passed into the function does match what it expects

# fav_num = int("seven")
# print(fav_num)

# FileNotFound Error
# with open("runtime_errors_note.txt", "r") as file_data:
#     content = file_data.read()

# print(content)
# print("File Read successfully")