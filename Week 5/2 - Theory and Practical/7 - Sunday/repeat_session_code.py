# Example 1

# Adding in values
# contact_info = {
#     "bartholomeow" : "barth@catmail.com",
#     "tom" : "tom@yahoocat.com",
#     "beans" : "beans@icat.com",
#     # "Tom" : "tom@yahoocat.com"    ==> avoid this, key mismatch and duplicate   
# }

# # Access values
# print(f"Tom's email: {contact_info['tom']}")

# # Add new contact
# # contact_info["sphinx"] = "sphinx@gcat@mail.com"
# contact_info.update({"sphinx":"sphinx@gcat@mail.com"})
# print(contact_info)

# # Remove a contact
# del contact_info['tom']
# print(contact_info)

"""
Best Practices
1. Use them when we can represent the data naturally as key-value pairs.
2. Make use of dictionary comprehension for concise dictionary creation
3. Be careful when modifying dictionaries or iterating over them. Key-Error handling
"""

# Dictionary Functions

# dict()
# Player Card
# user_name = input("Enter your character name: ")
# user_age = int(input("Enter your character's age: "))
# user_character_class = input("Enter your character class: ")

# # using dict() method
# character_dict = dict(name=user_name, age=user_age, character_class=user_character_class)
# # print(character_dict)

# # create players dictionary
# players_dict = dict(player_1=character_dict)
# print(players_dict)

# Dynamic Approach
# players_dict = {}

# for x in range(3):
#     user_name = input("Enter your character name: ")
#     user_age = int(input("Enter your character's age: "))
#     user_character_class = input("Enter your character class: ")

#     character_dict = dict(name=user_name, age=user_age, character_class=user_character_class)

#     players_dict[f"player_{x + 1}"] = character_dict

#     print("\n next player stats...")

# hardcoded values
players_dict = {
    "player_1": {'name': 'Haruki', 'age': 56, 'character_class': 'human'},
    "player_2": {'name': 'Paulo', 'age': 67, 'character_class': 'human'},
    "player_3": {'name': 'Fyodor', 'age': 908, 'character_class': 'human'}
}

# print(players_dict)

# print(f"The current players registerd are: {players_dict.keys()}")
# print(f"The current players stats are: {players_dict.values()}")


# iterating through dcitionary
# Keys in dictionary
# for key in players_dict:
#     print(key)

# values in dictionary
# for values in players_dict.values():
#     print(values)

# # items() function
# for key, value in players_dict.items():
#     print(key, value)

# # Get() - retrieval of information
# # The line `second_player = players_dict.get("player_5", "Player does not exist!")` is retrieving the
# # value associated with the key "player_5" from the `players_dict` dictionary. If the key does not
# # exist in the dictionary, it will return the default value "Player does not exist!".
# second_player = players_dict.get("player_5", "Player does not exist!")
# print("\n", second_player)

# # Pop() 
# second_player = players_dict.pop("player_2")
# print(second_player, "\n")
# print(players_dict)

# remove / clear all key-values
# print(f"Current Players in server: \n {players_dict.values()}")
# players_dict.clear()
# print("Cleared current players in server...")
# print(f"Current Players in server: \n {players_dict.values()}")


# copy()
copy_of_players_dict = players_dict.copy()
# print(copy_of_players_dict)

# fromkeys() - create dictionary from keys
new_players_list = ["player_4", "player_5", "player_6", "player_7"]
default_stats = {}

# creating new dictionary
# new_players_to_be_added = dict.fromkeys(new_players_list, default_stats)
# print("New dictionary", new_players_to_be_added)

# updating current dictionary
# players_dict.update(dict.fromkeys(new_players_list, default_stats))
# # print("Updated dictionary", players_dict)

# # popitem() - pop last key-value 
# last_player = players_dict.popitem()
# print(f"\nThe player removed is: {last_player}\n")
# print("Updated dictionary", players_dict)

# Dictionary comprehension

# List comprehension approach 
numbers_list = [1, 2, 3, 4, 5, 6]
squared_list = [num ** 2 for num in numbers_list]
print(f"Squared List: {squared_list}\n")

# Dictionary approach
numbers_list = [1, 2, 3, 4, 5, 6]
squared_dictionary = {num: num ** 2 for num in numbers_list}
print(f"Squared Dictionary: {squared_dictionary}\n")