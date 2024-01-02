# my_str = "Let's learn some more about strings"


# print(my_str.upper())

# print("Let's learn some more about strings".upper())

# upper_str = my_str.upper()
# print(upper_str)

# pass

# print(f"{upper_str}")

# =================================
# my_str = "Let's learn some more about strings"
# my_count = my_str.count("ea")
# print(my_count)

# =================================
# my_str = "Lat's learn some more about strings"
# my_find = my_str.find("Mikie")
# print(my_find)

# =================================
# my_alpha = "Mikie5$".isalnum()
# print(my_alpha)

# my_numeric = "12345".is
# print(my_numeric)

# =================================
# my_str = "      Let's learn some meare about strings     "
# new_str = my_str.strip()
# print(f">{new_str}<")

# new_lstr = my_str.lstrip()
# print(f">{new_lstr}<")

# new_rstr = my_str.rstrip()
# print(f">{new_rstr}<")

# # =================================
# new_repstr = new_str.replace("meare", "more")
# print(f">{new_repstr}<")

# =================================
# my_str = "Let's;learn;some;more;about;strings"
# my_list = my_str.split(";")

# print(f"split list: {my_list}")

# my_special_list = ["Let's", 'learn', 'some', 'more', 'about', 'strings']
# my_special_str = ";".join(my_special_list)

# print(f"join string: {my_special_str}")

# =================================
# my_special_list = ["Let's", 'learn', 'some', 'more', 'about', 'strings']
# my_special_list[-1] = "lists"

# print(my_special_list)

# Can't do the same with strings
my_sentence = "This is my mostest favouritous sentence of 2024!"
my_sentence[-2] = '3'           # This will give an error

# We can cast it to a list and make the change in the list
my_list = list(my_sentence)
print(my_list)
my_list[-2] = '3'
print(my_list)

# Now join it back to the string to get the change in the string
my_str = "".join(my_list)
print(my_str)
