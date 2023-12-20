"""
Challenge 1:
Create a for-loop that takes a base 
number and an exponent number and 
returns the calculation.
"""

# Challenge 1 : 5 * 5 = 3125
user_base = int(input("Enter base value: "))
user_expo = int(input("Enter exponent value: "))

total = 1

for value in range(user_expo):
    print(f"{total} * {user_expo}")
    total *= user_base
    # print(user_base)

print(f"{user_base} to the power of {user_expo} is: {total}")


"""
Challenge 2
Create a for loop that takes a list of numbers. 
Return the largest number in the list.
"""
# Challenge 2
list_of_numbers = [12, 34, 5, 678, 101, 0]
largest_num = 0

for num in list_of_numbers:
    if num >= largest_num:
        largest_num = num

print(f"The largest number in the list is: {largest_num}")

"""
Challenge 3
Create a for loop that takes a list of numbers and 
returns the smallest number in the list.
"""
# Challenge 3
list_of_numbers = [12, 34, 5, 678, 101]
smallest_num = list_of_numbers[0]

for num in list_of_numbers:
    if num <= smallest_num:
        smallest_num = num

print(f"The smallest number in the list is: {smallest_num}")

"""
Challenge 4

Create a for loop that takes a list and returns the difference between
the biggest and smallest numbers.
"""
# difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# # Smallest number is -50, biggest is 32.

# difference_max_min([44, 32, 86, 19]) ➞ 67
# # Smallest number is 19, biggest is 86.

# Challenge 4
list_of_numbers = [10, 4, 1, 4, -10, -50, 32, 21]
smallest_num = list_of_numbers[0]
largest_num = list_of_numbers[0]

for num in list_of_numbers:
    if num <= smallest_num:
        smallest_num = num
    if num >= largest_num:
        largest_num = num

value_difference = largest_num - smallest_num
print(f"The smallest number is: {smallest_num} \nThe largest number is: {largest_num} \n The difference is: {value_difference}")

# min max approach
# value_difference = max(list_of_numbers) - min(list_of_numbers)
# print(f"The smallest number is: {min(list_of_numbers)} \nThe largest number is: {max(list_of_numbers)} \n The difference is: {value_difference}")

"""
Challenge 5
Create a for loop that takes a list 
and returns the sum of all numbers in the list.
"""
# Challenge 5: The floor is yours
# Add your logic here: remember to use a for loop
