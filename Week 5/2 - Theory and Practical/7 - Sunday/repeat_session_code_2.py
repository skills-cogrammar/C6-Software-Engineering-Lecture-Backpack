from tabulate import tabulate

# Players Dictionary
players_dict = {
    "player_1": {'name': 'Haruki', 'age': 56, 'character_class': 'human'},
    "player_2": {'name': 'Paulo', 'age': 67, 'character_class': 'human'},
    "player_3": {'name': 'Fyodor', 'age': 908, 'character_class': 'human'}
}


# Printing out using for-loop
# for key, value in players_dict.items():
#     print(key, value)

# # Using Tabulate method
"""First Approach - Repeated stats"""
# The code `flattened_data = [(key, play, play_dict) for key, value in players_dict.items() for play,
# play_dict in value.items()]` is creating a flattened list of tuples from the `players_dict`
# dictionary. Each tuple in the list contains three elements: the key of the player dictionary, the
# key of the player's stats dictionary, and the player's stats dictionary itself.
flattened_data = [(key, play, play_dict) for key, value in players_dict.items() for play, play_dict in value.items()]
tabulated_data = tabulate(flattened_data, headers=["Player Name", "Player Key", "Player_stats"], tablefmt="grid")
print(tabulated_data)


""" Second Approach - Fixed""" 
# The code `flattened_data = [(key, value) for key, value in players_dict.items()]` is creating a
# flattened list of tuples from the `players_dict` dictionary. Each tuple in the list contains two
# elements: the key of the player dictionary and the player's stats dictionary itself.
flattened_data = [(key, value) for key, value in players_dict.items()]
tabulated_data = tabulate(flattened_data, headers=["Player Name", "Player Stats"], tablefmt="grid")
print(tabulated_data)


# List with nested dictionaries tabulated - Fixed
# The code is creating a list called `contact_info` which contains three dictionaries. Each dictionary
# represents contact information for a person, with the key being the person's name and the value
# being their email address.
contact_info = [
    {"bartholomeow" : "barth@catmail.com"},
    {"tom" : "tom@yahoocat.com"},
    {"beans" : "beans@icat.com"},
    # "Tom" : "tom@yahoocat.com"    ==> avoid this, key mismatch and duplicate
    ]

# The line `tabulated_data = tabulate(contact_info, headers="keys", tablefmt="pipe")` is using the
# `tabulate` function from the `tabulate` library to format the `contact_info` list of dictionaries
# into a table.
tabulated_data = tabulate(contact_info, headers="keys", tablefmt="pipe")
print(tabulated_data)