# create program to validate user password with booleans and conditionals.

"""
create constant bool variables: passwordLength, passwordCase and pass characters
create conditional checks for: length, upper and lowercase, character check
if conditional checks are true then change state of constant bool variables.
once determined, check password validity 
"""

pass_length_bool = False
pass_up_case_bool = False
pass_low_case_bool = False
pass_char_bool = False

# pass_length_bool = 0
# pass_up_case_bool = 0
# pass_low_case_bool = 0
# pass_char_bool = 0

length_prompt = input("Is the password longer than 6 characters ? yes or no ").lower()
if length_prompt == "yes":
    pass_length_bool = True

up_case_prompt = input("Does the password have uppercase characters ? yes or no ").lower()
if up_case_prompt == "yes":
    pass_up_case_bool = True

low_case_prompt = input("Does the password have lowercase characters ? yes or no ").lower()
if low_case_prompt == "yes":
    pass_low_case_bool = True

char_prompt = input("Does your password have odd characters ? yes or no ").lower()
if char_prompt == "yes":
    pass_char_bool = True

# Final Check - Using Bool int representation to perform mathematical operation
if (pass_char_bool + pass_length_bool + pass_up_case_bool + pass_low_case_bool) >= 3:
    print("You have a strong password!")
else:
    print("Your password is quite short!")
