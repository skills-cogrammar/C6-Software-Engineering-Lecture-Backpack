# Example 0

try:
    pass
    # operations like dividing by zero
    # or risky operations like openingg files
except:
    pass
    # for unforseen challenges or issues that may arise
    # code to handle that here

while True:
    user_input = int(input("How many cats do you have ? "))

    if user_input >= 3:
        print("YOu need more!")
        break
    else:
        print("are you even trying")

# Example 1
# integer try /except - 2 numerical values
try:
    user_age = int(input("How old are you really ? "))
except ValueError:
    print("Try entering it in as a number")


user_age = int(input("How old are you really ? "))
print("Try entering it in as a number")

# Example 2
# division by zero division error and a value Error in one block
try:
    num1 = int(input("Enter you first number: "))
    num2 = int(input("Enter you second number: "))

    output_result = num1 / num2

except ValueError as e:
    print("That is a colour! not a number")
    print(f"RIGHT HERE: {e}")
except ZeroDivisionError:
    print("Nice try!")
    print("Okay maybe try dividing against something other than zero")

# Example 3
# type error 
try:
    serge_age = 66
    serge_unique_skill = "ninja step"

    serge_combination = serge_age + serge_unique_skill

except TypeError as e:
    print("This doesn't make sense, there is a type mismatch")
    print(f"for more detail read this: {e}")

# Example 4
# zero division with else and finally 
try:
    num1 = int(input("Enter you first number: "))
    num2 = int(input("Enter you second number: "))

    output_result = num1 / num2
except ZeroDivisionError:
    print("Nice try!")
    print("Okay maybe try dividing against something other than zero")
else:
    print("Division successful. Well Done!")
finally:
    # the block runs whether there's an error or not.
    # event trigger to relay information to dev 

# try
# except
# else
# finally

# Example 5
# file I/O with else and finally

try:
    file_path = "list_of_cats.txt"
    with open(file_path, "r") as file_data:
        content = file_data.readlines()
except FileNotFoundError:
    print("The file does exist or has not been found.")
else:
    print("File has been loaded, feed the true gods (the cats)")
finally:
    # print("cats meow meow")
    pass

# Example 6
# incorporating  a while loooooooooooooop 
# zero division with else and finally 
    
while True:
    try:
        num1 = int(input("Enter you first number: "))
        num2 = int(input("Enter you second number: "))

        output_result = num1 / num2
      
    except ValueError:
        print("That is not a number, please try again")
    except ZeroDivisionError:
        print("Nice try! Enter a value other than zero")
    else:
        print("Thank you, remember to vote for pluto as a planet")
        break
    
# file I/o with while loop and try/body
# challenge (Pluto believes in you 💪)

# raise example 
num1 = 10
num2 = 0

if num2 == 0:
    raise ZeroDivisionError("Cannot divide by zero")
