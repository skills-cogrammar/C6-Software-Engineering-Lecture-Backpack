""" ===== Different list examples ===== """

# ========================== Creating a list
new_list = []
word_list = ["word1", "word2", "word3"]

# -- Dealing with boolean lists
bool_list = [False, True, True, False]
bool_list = [0, 1, 1, 0]

my_bool = bool(bool_list[0])
my_bool = bool(0)       # my_bool = False

if my_bool == False:
    pass

if my_bool:       # Conditions always test for True or False (Here: if True)
    pass

if not my_bool:     # (Here: if not True)
    pass

bool_list = [False, True, True, False, "Word1"]
for item in bool_list:
    if item:            # If True
        print("The value is True")
    elif not item:      # If False
        print("The value is False")
    else:
        print("The value is not a boolean")

student_number = [1, 2, 3, 4]
pass_result = [False, True, True, False]
for student in range(len(student_number)):
    if pass_result[student]:            # If True
        print(f"Student {student_number[student]} : passed")
    elif not pass_result[student]:      # If False
        print(f"Student {student_number[student]} : failed")
    else:
        print(f"Student {student_number[student]} : result unknown")

# -- Dealing with mixed lists
mixed_list = ["Hello", 13, 87.89, True, None, (), [1, 2, 3, ['a', 'b', 'c']], {}]
my_item = mixed_list[6][3][1]       # Access the 'b'

# -- Create lists with casting
# Data types that we can cast to a list
my_string = "Hello"
my_list = list(my_string)
print(my_list)

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)

my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_keys = list(my_dictionary.keys())
print(list_from_keys)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_values = list(my_dictionary.values())
print(list_from_values)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list_from_items = list(my_dictionary.items())
print(list_from_items)

# -- Creating lists with the range
# Normally we will have
for even_num in range(2, 11, 2):
    print(even_num)

# Another option to above
my_range = list(range(2, 201, 2))
print(my_range)

for even_num in my_range:
    print(even_num)

# -- List dimensions
# 1-dimensional list
num_list = [1,2,3,4,5]

# -- Creating a 2-dimensional list
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]

my_item = list_2[1]

list_2d =  [[1,2,3], 
            [4,5,6], 
            [7,8,9]]

my_item = list_2[1][1]

# -- Creating a 3-dimensional list
list_3d =  [[[1,2,3], [4,5,6], [7,8,9]],
            [[11,12,13], [14,15,16], [17,18,19]],
            [[21,22,23], [24,25,26], [27,28,29]]]

my_item = list_3d[2][1][1]			#Refer to value 25

# -- Setting a list to another list - BE WARNED (This can create a logic error)
num_list = [1,2,3,4,5]
new_num_list = num_list

new_num_list[2] = 200

num_list_sum = sum(num_list)		# Answer is 212 which is not what we expected
print(f"-- The sum of the items in num_list is {num_list_sum}.")

print(num_list)             # The 3rd value in num_list will also change to 200

# -------------  To prevent the above use the copy method

num_list = [1,2,3,4,5]
new_num_list = num_list.copy()

new_num_list[2] = 200

num_list_sum = sum(num_list)		# This answer is 15 which is what we are looking for.
print(f"-- The sum of the items in num_list is {num_list_sum}.")

print(num_list)


