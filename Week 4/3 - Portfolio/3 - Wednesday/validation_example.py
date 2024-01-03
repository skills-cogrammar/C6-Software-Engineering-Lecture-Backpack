import re

user_email = input("Enter you email address: (e.g yourname@mail.com)")

# Email - approach 0 
# if "@" in user_email and "." in user_email:
#     print("Your email is valid!")

# else:
#     print("Your email is invalid")

# Email - approach 1
email_pattern = r'^\S+@\S+\.\S+$'

#   "^" - caret or roof (welsh)

expected_match = re.match(email_pattern, user_email)

if expected_match is None:
    print("Enter email address")
elif expected_match:
    print("The email is valid!")
    print(f"Email Validitity: {expected_match}")
else:
    print("The email is invalid!")
    print(f"Email Validitity: {expected_match}")
