# Booleans can only be stored as one of two things: True or False
# Mainly use them for conditional checks

# Booleans should also be declared with Capital Letters, NB using lowercase will result in errors

light_switch = True
light_switch = False

# light_switch = true
# light_switch = false

# x = 1 TRUE
# x = 0 FALSE

# x = "" FALSe
# x = None False
# x = 0 False 

# num_one = 0
# print(bool(num_one))

# num_two = 12.3
# print(bool(num_two))

"""
Control structures are basically statements that will analyse variables 
or decisions to choose a direction to follow based on the input provided.
"""

"""
if I finish my work early, I get to play elden ring for the next hour
else I will have to resort to a comfort game like bloodborne
"""

"""
if I finish my work early, I get to play a game
    if I am feeling like a God then I play bloodborne
    else I play elden ring
else I continue work and go to bed
"""


# if <condition>
#     <statement>
# elif <condition>
#    <statement>
# elif <condition>
#   <statement>
# else
#     <fall back statement>

# Crisps or chocolate example 
# snack_option = input("Would you like a crisp or chocolate ? enter CR-Crips : CH-Choco")

# IF ELIF STATEMENT
if snack_option == "CR":
    print("You have chosen crisps")
elif snack_option == "CH":
    print("You have chosen Chocolate")
else:
    print("You have entered an invalid option, please try again")

# NESTED STATEMENTS
student_grade = int(input("Enter your grade: "))

if student_grade > 50:
    if student_grade > 75:
         print("You passed with distinctions")
    else:
         print("You passed, but you can do better!")
else:
     print("You failed but this is a learning milestone")
