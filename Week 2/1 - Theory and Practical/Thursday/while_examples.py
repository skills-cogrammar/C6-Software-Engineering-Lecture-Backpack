"""WHILE LOOPS"""

# Example 1: Print numbers from 1 to 5 using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# ???? Is there an alternative to above?
    
# Example 2: Repeatedly prompt the user until valid input is received
user_input = ''
while user_input.lower() != 'yes':
    user_input = input("Do you want to continue? (yes/no): ")

# Example 3: Calculate the sum of numbers until a certain condition is met
total = 0
num = 1
while total < 10:
    total += num
    num += 1
print("Sum:", total)

# Example 4: Interactive Menu
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

# Example 5: Number Guessing Game
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

# ???? How can we change the above to remove the break statement