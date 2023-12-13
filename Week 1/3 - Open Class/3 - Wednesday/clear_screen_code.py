""" Code to clear the console in the code logic """

# ===== Importing libraries =====
import os

# You can either code a simple function which we will address later
def clear_screen():
    os.system("cls||clear") 

# Call the function whenever you want to clear:
clear_screen()

# Here is some test code for using the function
print("I am printing")
clear_screen()
print("The screen is cleared")

# =================================================================
# If you are not ready for function, just add the code in the logic
# You must still import the os library to use the system module
os.system("clear||cls") 

# Here is some test code for not without using the function
print("I am printing")
os.system("clear||cls") 
print("The screen is cleared")

# =================================================================
# To clear the screen manually, just enter clear in the console 
