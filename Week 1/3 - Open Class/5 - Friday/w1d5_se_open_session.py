""" This is a Open Class demonstration """

# === Different data types
# -- From Task 1
# my_string = "This is my mostest favoritous sentence"
# my_integer = 5
# my_float = 4.89
# my_boolean = False

# -- Still to come
# my_list = []
# my_set = {a, b}
# my_dict = {a: value1, b: value2}
# my_tuple = ()

# === Using string indexing
friendly_greeting = 'Hello World!'

# ' H e l l o w o r l d ! '
# my_str_lst = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"]
#                0    1    2    3    4    5    6    7    8    9   10    11

# -- string slicing (Start with the step) 
# format => string[start(incl):end(excl):step]

print(friendly_greeting[1:5:1]) # print "ello"
print(friendly_greeting[4:0:-1]) # print "olle"

# === Using the not logical operator - See not_operator_demo.py

# # === Understanding logic flow to negate using ranges
# student_grade = 62

# # A-Grade for students with grade 90 and above
# if student_grade >= 90:
#     print("A Grade")

# # B-Grade for students with grade 80 and above, but less than 90
# elif student_grade >= 80: # and student_grade < 90
#     print("B Grade")

# # C-Grade for students with grade 70 and above, but less than 80
# elif student_grade >= 70: # and student_grade < 80
#     print("C Grade")

# # D-Grade for students with grade 60 and above, but less than 70
# elif student_grade >= 60: # and student_grade < 70
#     print("D Grade")

# # Rewrite for students with grade less than 60
# else:
#     print("Don't leave for next year what can be done this year!")
    