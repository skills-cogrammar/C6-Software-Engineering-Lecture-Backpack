import random

# Create a rock paper scissors game, Player vs Computer

"""
* create random number generator for computer within range(1, 3) to 
represent a hand
* attach numerical values to hands: 1 = rock; 2 = paper; 3 = scissors
through conditional check
* Asking the user to pick a hand, create numerical input
* Play the game: conditional structure comparing user hand against 
computer hand
* Return who has won
"""

# 1 = rock; 2 = paper; 3 = scissors

rand_value = random.randint(1, 3)
# print(f"Current Random Number: {rand_value}")

# attaching user hand to either rock; paper; scissors
comp_hand = ""

if rand_value == 1:
    comp_hand = "Rock"
elif rand_value == 2:
    comp_hand = "Paper"
elif rand_value == 3:
    comp_hand = "Scissors"
else:
    comp_hand = "nah"   # default value

# Get user input / hand
user_hand = int(input("Pick a hand: \n1 - Rock \n2 - Paper \n3 - Scissors \n: "))

user_hand_word = ""

if user_hand == 1:
    user_hand_word = "Rock"
elif user_hand == 2:
    user_hand_word = "Paper"
elif user_hand == 3:
    user_hand_word = "Scissors"
else:
    user_hand_word = "nah"   # default value

# Core Game Logic
# Three outcomes: computer wins, user wins, draw

print(f"👻 You have chosen {user_hand_word} \n🦄 Computer has chosen {comp_hand}")

#                   (true)              or                  (true)              or                 (true)   
#       (true        and     true)      or      (true        and     true)      or      (true        and     true)  
if ((rand_value == 1 and user_hand == 3) or (rand_value == 2 and user_hand == 1) or (rand_value == 3 and user_hand == 2)):
    print("The computer has won this round!")

elif ((user_hand == 1 and rand_value == 3) or (user_hand == 2 and rand_value == 1) or (user_hand == 3 and rand_value == 2)):
    print("💫 You are smarter than the AI overlords, you beat the computer! 💫")

elif user_hand == rand_value:
    print("This is a draw.")

# else:
#     print("An error in our logic has occured!")
