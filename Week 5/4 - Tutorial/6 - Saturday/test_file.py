print("all animals deserve lurv")

user_var = input("Enter your name: ")

# The code is printing a mesage "so to spell your name out, it's: " and
# then iterating over each
# character in the user's inputed name (`user_var`). For each character,
# it is printing the character
# on a new line.
print("so to spell your name out, it's: \n")
# The code `for letter in user_var: print(letter)` is iterating over each character in the string
# stored in the variable `user_var`. For each character, it is printing the character on a new line.
for letter in user_var:
    print(letter)

# ctrl + .

# cmd + .
    

def program_Owner(name):
    """
    The function `program_Owner` takes a name as input and prints a message stating that the name is the
    owner of the program.
    
    :param name: The name of the program owner
    """
    print(f"{name.upper()} is the owner of this program!")


# program_Owner("Serge")

# Reading From File
# The code is opening a file named "cat_names.txt" in read mode using the `open()` function. It then
# assigns the file object to the variable `file`.
with open("cat_names.txt", "r") as file:
    cat_names_list = file.readlines()
    for x in cat_names_list:
        print(x)

print(cat_names_list)


def print_name():
    """
    The function `print_name` prints the name "Serge".
    """
    print("Serge")


print_name()
