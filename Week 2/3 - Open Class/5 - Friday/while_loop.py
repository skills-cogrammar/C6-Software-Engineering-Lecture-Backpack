# while loop
"""
while condition:
    execute logic as long as condition is true
"""

# Example 1
count = 1
while count <= 5:
    print(count)
    count += 1

# Example 2
i = 5

while i < 14:
    print("I can see infinity")

# Example 3
# Multiplication table

user_num = int(input("Enter a number: "))

# Using a for loop
for x in range(10):
    print(f"{x} x {user_num} = {x * user_num}")
count = 1

# Using a while loop
while True:
    print(f"{count} x {user_num} = {count * user_num}")
    count += 1

    if count == 11:
        break

# Example 4
# atm menu with String inputs
while True: 

    user_input = input("""Please pick an option: \nd- Deposit 
w - Withdraw \ncb - Check Balance \ne - Exit \n: """).lower()
    
    if user_input == "d":  
        pass
    elif user_input == "w":
        pass
    elif user_input == "cb":
        pass
    elif user_input == "e":
        print("Goodbye, your money is safe with us... or is it ? ")
        break
    else:
        print("incorrect option chosen!")

# Numerical inputs and try/except
while True: 
    try:
        user_input = int(input("""Please pick an option: \n1- Deposit 
    2 - Withdraw \n3 - Check Balance \n4 - Exit \n: """))
        
        if user_input == 1:  
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            print("Goodbye, your money is safe with us... or is it ? ")
            break
        else:
            print("incorrect option chosen!")
    except ValueError:
        print("Try to enter numerical values only!")

# Example 5
my_password = "goku123"
attempts = 0
max_attempts = 3

while attempts <= max_attempts:
    user_pass = input("Enter the password: ")

    if user_pass == my_password:
        print("You have been granted access to my entire digital life")
        break
    else:
        print("hahaha incorrect password! ")

    attempts += 1

if attempts == max_attempts:
    print("Multiple incorrect attempts. Access Denied. FBI Informed!")


# Functions Examples
def password_check():
    my_password = "sergeCat"
    attempts = 0
    max_attempts = 3

    while attempts <= max_attempts:
        user_pass = input("Enter the password: ")

        if user_pass == my_password:
            print("You have been granted access to my entire digital life")
            break
        else:
            print("hahaha incorrect password! ")

        attempts += 1

    if attempts == max_attempts:
        print("Multiple incorrect attempts. Access Denied. FBI Informed!")


# function to perform addition
def addition(a, b):
    return a + b


# Function call with parameters / arguments
print(addition(4, 5))

# Function
password_check()
