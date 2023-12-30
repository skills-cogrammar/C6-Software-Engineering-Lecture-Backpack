# Error 1
# calculate average
# num1 = 10
# num2 = 20
# num3 = 30

# # incorrect average
# average = (num1 + num2 + num3) / 3

# print(f"Average: {average}")
# print(f"Correct average: {average}")

list_of_numbers = [12, 23, 34, 45, 56]
# total = 170
# count = 5

total = 0
count = 0

for num in list_of_numbers:
    total += num
    count += 1

    print(f"Current value of total: {total}")
    print(f"Current value of count: {count}")

# average = 34
print(f"Average: {total/count}")

# Error 2
# num1 = 0

# if num1 < 0:    # missing equal sign
#     print("Negative or zero")
# else:
#     print("Positive")

# Error 3
# count = 0
# while count % 2 == 0:
#     print(count)
#     count += 2

# Error 4
# count = 4

# if count % 2 == 0:
#     print("Even")
# elif count % 2 == 1:    # Elif Not necessary
#     print("Odd")
# else:
#     print("Neither even nor odd")

# Error 5
# user_num = 5689

# if user_num > 20 and user_num < 60:      # use of or statement
#     print("Your number is between 20 and 60")
# else:
#     print("Your number falls outside our range")

# Error 6
# user_num = 5689

# if user_num % 2 == 1 and user_num % 2 == 0:
#     print("Your number is both odd and even")
# else:
#     print("Your number is either odd or even")

# print(int(False))
