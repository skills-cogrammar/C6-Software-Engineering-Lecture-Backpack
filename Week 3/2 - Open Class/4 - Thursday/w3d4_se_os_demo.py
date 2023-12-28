

# Example 1: Interactive Menu - Dealing with string numbers
choice = ''
while choice != '3':            # while True - Less favourable option
    print("Menu:\n"
            "1. Option 1\n"
            "2. Option 2\n"
            "3. Exit")

    choice = input("Enter your choice: ")

    # Perform Option 1 logic
    if choice == '1':
        print("You chose Option 1.")

    # Perform Option 2 logic 
    elif choice == '2':
        print("You chose Option 2.")
    
    # Perform Option 3 logic
    elif choice == '3':
        print("Exiting the program.")
        # while loop will exit naturally with this option 
        # break statement is need here with while True while dondition

    # Process invalid menu choices
    else:
        print("Invalid choice. Please try again.")

print("--- Continue with logic ---")

# Example 2: Number Guessing Game - Dealing with numeric numbers
import random

target_number = random.randint(0, 100) # Function outside standard library
attempts = 0

print(f"Random Number: {target_number}")

while True:
    guess = input("Enter your guess (between 0 and 100): ")

    if not guess.isdigit() or int(guess) <= 0 or int(guess) >= 100:
        print("-- Invalid number")
        continue
    else:
        guess = int(guess) # No need for error-handling: number confirmed
    
    attempts += 1

    if guess == target_number:
        print(f"Congratulations! You guessed the correct number "
              f"{target_number} in {attempts} attempts.")
        break
    elif guess < target_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

# Example 3: Multiple input example - Dealing with string inputs
while user_input.upper() not in ["STOP", "EXIT", "END"]:
    print("Hello")
    user_input = input("Please press enter or enter the word 'stop': ")

# Above example for an option input list, ie. cities to travel or menu options

# --- Operators input ------

operators_list = ['+', '-', '*', '/']

operator_input = ''
while operator_input() not in operators_list:
    operator_input = input("Please provide the operator for your calculation "
                           "(+, -, *, /): ")
	

