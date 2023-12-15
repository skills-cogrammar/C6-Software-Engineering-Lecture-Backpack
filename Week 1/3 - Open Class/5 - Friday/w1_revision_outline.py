""" What did we address in Task 1 to Task 5 for this week?"""

# -- Task 1: Your First Computer Program and Using Variables

# print() - function
# input() - function
# variable data types: strings, chars, integers, floats, Booleans
# type() - function

# casting variables

# f-string, ie f"{name} {name}"
# .format, ie. "{1} {0}".format(name, surname)

# -- Task 2: The String Data Type

# What are strings?
# Numbers as strings
# Multi-line strings

# Line wrapping
print("If you can bark, \
does that mean you are a dog?")

print("If you can bark, "
    "does that mean you are a dog?")

print(f"If you can bark, "
    f"does that mean you are a dog?")

# String formatting - you can only concatenate strings
# String indexing - string is a list of one character values

# escape characters \n, \t

# len() - function
# slicing [begin, end, step] # See w1d5_se_open_session.py for example
# .upper(), .lower(), .title, .capitalize methods

# Functions operates standalone / Methods are object specific
my_int = 5
# Cannot do an .upper() method on an integer, it is string specific
my_int.upper()  

my_str = "a$"
my_str.upper()

# my_str.replace() is a string specific method
my_str.replace("$", "")
         
# my_sentence.strip() method - Only removes front and back. 
my_sentence = "$$$$$$super$man$$$$$$"
my_sentence.strip("$")
result = "super$man"

# Use this to also prepare input. Ask user for input
my_input = "London     "
if my_input == "London":   # False since input has trailing spaces
    pass

# -- Task 3: Control Structures: If, Elif, Else, and the Boolean Data type

# if Statements
# Comparison Operators
# Booleans
# Structure of if-else statements - See w1d5_se_open_session.py for example

# -- Task 4: Logical Programming – Operators

# Comparison operators (==, !, >, <)

# Difference between = and ==
# Logical Operators (and, or, not)
# Arithmetic Operators (+, -, *, /, %, **)
# Assignment Operators (=, +=, -=, /=, etc.)

# ** Triathlon  task

# -- Task 5: Capstone Project - Variables and Control Structures

# ** Finance Calculator Task

# import math
