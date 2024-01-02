""" Examples for try-except concept"""
try:
    pass
    pass
    pass
    pass

except ValueError as v_error:
    pass

except ZeroDivisionError as div_error:
    pass

except Exception as error_message:
    print(error_message)

else: 
    pass

finally:
    pass

#========================

valid_number = False
while not valid_number:
    try:
        user_num = int(input("Please provide a number above 100: "))
        if user_num <= 100:
            raise ValueError

        valid_number = True

    except ValueError:
            print("You did not enter a valid number!")

#========================
valid_number = False
while not valid_number:
    try:
        user_num1 = int(input("Please provide a number: "))
        user_num2 = int(input("Please provide another number: "))

        result = user_num1 / user_num2  #Lookout for zero division
        if user_num2 == 0:
            raise ZeroDivisionError

        valid_number = True

    except (ValueError, ZeroDivisionError) as er_message:
            print("You did not enter a valid number!")
            print(er_message)

#==============================
try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
    print("This line will not be executed.")
except FileNotFoundError as my_error:
    print(f"An unexpected error occurred: {my_error}")

except Exception:
     pass

# type error 
try:
    john_age = 66
    john_unique_skill = "ninja step"

    serge_combination = john_age + john_unique_skill

except TypeError as e:      # Because cannot concatenate int with str
    print("This doesn't make sense, there is a type mismatch")
    print(f"for more detail read this: {e}")

