# Zero Division - Example 1
# try:
#     num1 = 34
#     num2 = 2

#     result_var = num1 / num2
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print(f"The result of {num1} / {num2} is {result_var}")


# Input Conversion - Example 2
# try:
#     user_age = int(input("Enter your age: (the real one Serge) "))
# except ValueError:
#     print("Try adding your age as a numerical value!")
# else:
#     print(f"Thank you for being alive for {user_age} years!")

# While - Except
# # The code snippet is using a `while` loop to repeatedly ask the user to enter their age until a
# valid numerical value is provided.
# while True:
#     try:
#         user_age = int(input("Enter your age: (the real one Serge) "))
#     except ValueError:
#         print("Try adding your age as a numerical value!")
#     else:
#         print(f"Thank you for being alive for {user_age} years!")
#         break

while True:
    # The program breaks out once the user enters zero, how can we repropmt to enter a value ?
    user_order = input("""
Welcome To McSerge's!
        Add Order - A
        Pick up Order - P
        Donate - D
        Exit - E
""").upper()
    
    if user_order == "A":
        pass
    elif user_order == "P":
        pass
    elif user_order == "D":
        while True:
            try:
                user_amount = int(input("Enter donation amount: or -1 to return to menu "))
                if user_amount == -1:
                    break
                elif user_amount == 0:
                    print("You can't donate nothing! The cats will starve")
            except ValueError:
                print("Enter a numerical value")
            else:
                break
    elif user_order == "E":
        print("Thank you for coming to McSerge's! Grab a kitten on the way out")
        break
    else:
        print("invalid input has been entered!")
