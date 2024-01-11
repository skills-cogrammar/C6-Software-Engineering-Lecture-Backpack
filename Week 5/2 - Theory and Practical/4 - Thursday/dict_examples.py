# Example 1 - Creating a dictionary

# # cat_dict = {"name": "bartholomeow", "age": 12, "city": "Paris", "breed": "Burmese"}
# cat_dict = dict(name="bartholomeow", age=12, city="Paris", breed="Burmese")
# print(cat_dict)

# # Access value
# # breed_var = cat_dict["breed"]
# # print(breed_var)

# breed_var = cat_dict.get("Breed")
# print(breed_var)

# # Changing or updating particular values
# cat_dict["breed"] = "York Chocolate"
# print(cat_dict)

# Example 2

cats_dict = {"Bartholomeow": "Bermese", "Garfield": "Orange", "Tom": "Egyptian Mau", "Beans": "Persian" }
print(cats_dict)
# Looping
# Traditional - Option 1
# for key in cats_dict:
#     print(key, cats_dict[key])

# Values - Options 2  
# for value in cats_dict.values():
#     print(value)

# Keys - Option 3
# for key in cats_dict.keys():
#     print(key)   

# for key, value in cats_dict.items():    # ("Bartholomeow", "Bermese")
#     print(f"{key}: {value}")


# Can we use:
# print(cat_dict.keys()) ?
# print(cats_dict.keys())

# key_list = list(cats_dict.keys())
# print(key_list)

# Removing Items from dictionary
# Option 1
# cats_dict.pop("Tom")
# print(cats_dict)

# Option 2

# cats_dict.popitem()
# print(cats_dict)

# last_cat = cats_dict.pop("Tom")
# print(last_cat)

# last_cat = cats_dict.popitem()
# print(last_cat)

# Option 3
# cats_dict.clear()
# print(cats_dict)