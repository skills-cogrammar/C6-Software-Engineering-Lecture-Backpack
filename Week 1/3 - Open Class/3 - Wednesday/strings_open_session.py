""" This is a C6 Open Session Demonstration """

# ======================== String Literals =========================

# -- Single quotes --
# single_quote = 'A'

# -- Double quotes --
# double_quote = "The quick brown fox jumps over the lazy dog"

# -- Quotes in quotes --
# quote_in_quote = "Join said 'I love this session.'"
# print(quote_in_quote)

# -- Triple quotes (Multi-line) --
# multi_line_string = """This is a
# multi-line
# string."""

# print(multi_line_string)
# print()

# ======================== Escape Characters =========================

# -- Only one set of double quotes used here
# multi_line_esc_string = "This is a\nmulti-line\nstring."
# print(multi_line_esc_string)
# print()

# ======================== Concatenation =========================

# Assigning a string to a variable
name = "Miles"
surname = "Morales"

# -- Assigning the result of two concatenated strings 
# -- to a variable called 'full_name'
# full_name = name + surname
# print(full_name)

# full_name = name + " " + surname
# print(full_name)

# ======================== Formatted Strings =========================

# -- f-strings
# show_friend = f"My friend {name} has the {surname} surname."
# show_friend = f"{name} {surname}"

# print(show_friend)

# -- .format
# name = "Miles"
# age = 30

# greeting = "Hello, my name is {} and I am {} years old.".format(name, age)
# print(greeting)

# -- Change variable order
# greeting = "Hello, my name is {1} and I am {0} years old.".format(name, age)
# print(greeting)

# ======================== Raw Strings =========================

# print()
# raw_string = r"This is a\nraw\nstring."
# print(raw_string)
# print()

# multi_line_esc_string = "This is a\nmulti-line\nstring."
# print(multi_line_esc_string)
# print()

# ===== Printing a user-friendly output to the terminal =====

# print("========= Introducing my friend ========\n")
# full_name = "Riaan Deventer"
# print(f"My name is {full_name}")
# print(f"My friend's name is {name} {surname}")
# print('=' * 50)
