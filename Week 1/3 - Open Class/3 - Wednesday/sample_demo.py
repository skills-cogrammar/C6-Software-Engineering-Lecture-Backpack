""" This is a Open Class demonstration """
"""
print()             # This is a function
input()             # This is a function
my_string.upper()   # This is a method
"""

# === Different kind of inputs
"""
1. Hardcode, ie. name = "Myles"
2. input(), ie.
"""
name = input("Enter your name: ") # user inputs Myles
"""
3. read from file           # Will address later in course
4. read from a database
"""

# === Different kind of outputs
"""
1. print(), ie.
"""
print(name)
"""
2. write from file          # Will address later in course
3. write from a database
"""
# === Using the type() function to identify data types
my_int = 5
my_str = "5"

# Only printing variable content shows no difference
print(my_int)
print(my_str)

# The below prints include the data type and differenciates
print(f"{my_int} type: {type(my_int)}")
print(f"{my_str} type: {type(my_str)}")
