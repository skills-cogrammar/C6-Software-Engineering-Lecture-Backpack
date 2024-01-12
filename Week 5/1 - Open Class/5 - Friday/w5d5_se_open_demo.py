# -- Creating a dictionary
my_dictionary = {"name": "Mikie", "age": 25, "coming_from_city": "New York", "moved_to_city": "London"}

# -- Move the keys into a list
my_keys_list = list(my_dictionary.keys())
print(my_keys_list)                 # ['name', 'age', 'coming_from_city', 'moved_to_city']

# -- Another option to the above
# my_key_list = list(my_dictionary)   
# print(my_key_list)                # ['name', 'age', 'coming_from_city', 'moved_to_city']

# -- Below not working. Error: ValueError: dictionary update sequence element #0 has length 4; 2 is required
# casted_dictionary = dict(key_list)
# print(casted_dictionary)

# # How to solve casted_dictionary = dict(key_list)
# casted_dictionary = dict(name = "Mikie", age = 25, coming_from_city = "New York", moved_to_city = "London")
# print(casted_dictionary)

# ============== How to iterate through dictionary
for key in my_keys_list:
    value = my_dictionary[key]
    print(value)

# === With above - Iterating Over Keys, Values, and Items:

# Iterating over keys
print('-' * 30)
for key in my_dictionary:
    print(key)

# Iterating over values
print('-' * 30)
for value in my_dictionary.values():
    print(value)

# Iterating over key-value pairs
print('-' * 30)
for key, value in my_dictionary.items():
    print(f"{key}: {value}")

"""
The key and value variables used in the last for loop can be any name? 
"""
print('-' * 30)
# Both Keys & Values
for i, j in my_dictionary.items():
    print(f"Key: {i}\nValue: {j}\n")

# ??? Learner Question: Is there a way to temporarily store the last value in a dict to a variable?
my_dictionary = {"name": "Mikie", "age": 25, "coming_from_city": "New York", "moved_to_city": "London"}

# Use popitem() to get the last key-value pair in a dictionary
last_key, last_value = my_dictionary.popitem()

print(f"Last key: {last_key}")
print(f"Last value: {last_value}")

# ============== Using a key to access a value
print(my_dictionary["name"])

# -- Using the the key to add or update values
my_dictionary["gender"] = "Lady"        # Adding a key value
my_dictionary["age"] = 16               # Updating the value of an existing key 

print(my_dictionary)

# ============== Using get() to check if a key exists
my_dictionary = {"name": "Mikie", "age": 25, "coming_from_city": "New York", "moved_to_city": "London"}
result = my_dictionary.get("name", "Student not yet registered")
# Above returns name value if key is found else display the default 
# provided: "Student not yet registered" in this case.
print(result)

# Using "in" to check if a key exists
if "name" in my_dictionary:
    print("Name exists in the dictionary")

# ========== Additional Content
# Removing a key-value pair using del
del my_dictionary["city"]

# Removing a key-value pair using pop()
age = my_dictionary.pop("age")

# ==========  Creating a new dictionary using comprehension
squared_values = {key: value**2 for key, value in my_dictionary.items()}

# ??? Learner Question: Please show example of list comprehension
nested_list = [[i for i in range(3)] for _ in range(3)]
print(nested_list)

 ==================   List operations

# ========================== Adding items

my_list = ["This", "is", "our", "list", "!"]
print(my_list)
# Consider the application of methods because of mutability

my_list.append(":-)")
print(f"append: {my_list}")

my_list.insert(2, "insert")
print(f"insert: {my_list}")

my_list.extend(["This", "is", "another", "list", "."])
print(f"extend: {my_list}")

my_list += ["This", "is", "another", "list", "."]
print(f"concatenate: {my_list}")

# for the above with values, we can asign the value to a variable and use the
# variable in the method
my_list = ["This", "is", "our", "list", "!"]
another_list = ["This", "is", "another", "list", "."]
my_list.extend(another_list)
print(f"extend: {my_list}")

# ========================== Removing items

my_list = ["This", "is", "our", "list", "!"]

my_list.remove("list")      # remove item by value
print(f"remove list: {my_list}")

my_list.pop(0)              # remove item by position number
print(f"pop 1st position: {my_list}")

my_list.clear()             # empty the list, but variable still exists
print(f"clear: {my_list}")

my_list = ["This", "is", "our", "!"]    # Same as after remove above
del my_list[0]              # remove item by position number
print(f"del position: {my_list}")

del my_list                 # remove value and variable from memory
print(f"del list: {my_list}")

# ========================== List manipulation

my_list = ["This", "is", "our", "list", "!"]

my_list.sort()
print(f"sort: {my_list}")

my_list.reverse()
print(f"reverse: {my_list}")
