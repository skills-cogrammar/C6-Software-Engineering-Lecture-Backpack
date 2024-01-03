# Steps to Hypothesis Driven Debugging
# 1 - Observations
# 2 - Question
# 3 - Form Hypothesis
# 4 - Make Prediction 
# 5 - Test it out


# Example 1
# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# results = num1 - num2
# print(f"{num1} - {num2} = {results}")

# Example 2
# counter = 5

# print("New year count down!! ")
# while counter > 0:
#     print("Counter: ", counter)
#     counter -= 1

# Example 3 
# # (0, 1, 2, 3, 4)
# for i in range(5):
#     print(f"Number: {i + 1}")

# Example 4
# for i in range(1, 5):
#     print(f"\n **** Current Outer Loop value: {i} **** \n")
#     for j in range(1, 5):
#         print(f"Current Inner Loop value: {j}")
#         result = i / j
#         print(f"Results: {result}")

# Example 5
# my_list = [12, 23, 34, 45, 56]

# prediction 1
# for i in range(0, 5):
#     value = my_list[i]
#     print(f"The current value at index {i + 1} is: {value}")

# prediction 2
# for i in range(len(my_list)):
#     value = my_list[i]
#     print(f"The current value at index {i + 1} is: {value}")

# prediction 3

#            0   1    2   3   4   5
# my_list = [12, 23, 34, 45, 56]


# for count, i in enumerate(my_list, 1):
#     print(count)
#     value = my_list[count - 1]
#     print(f"Current item in variable: {value}")
#     # print(f"The current value at index {count} is: {value}")


# Working Example 6
# list_of_smort_numbers = [12, 23, 34, 45, 56]

# for i in range(len(list_of_smort_numbers)):
#     list_of_smort_numbers[i] += 1

# print(f"Updated Numbers: {list_of_smort_numbers}")

# Exercise - debug this
# Ex 1
list_of_smort_numbers = [12, 23, 34, 45, 56]

for i in range(len(list_of_smort_numbers)):
    list_of_smort_numbers[i] += 1

print(f"Updated Numbers: {list_of_smort_numbers}")

# Ex 2
list_of_smort_numbers = [12, 23, 34, 45, 56]

total = sum(list_of_smort_numbers)
count = len(list_of_smort_numbers)

average = total / count

print(f"Total: {count}")
print(f"Average: {average}")