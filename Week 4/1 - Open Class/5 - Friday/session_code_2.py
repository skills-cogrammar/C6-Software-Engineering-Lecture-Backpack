# obtaining a value from list
# my_pokemon = ["squirtle", "metapod", "pikachu", "charizard", "gengar"]

# print(f"I choose you {my_pokemon[2]}")

# # adding items to the list
# my_pokemon.append("gastly")
# print(my_pokemon)

# # inserting items to specific position in list
# my_pokemon.insert(3, "charmander")
# print(my_pokemon)

# # taking one item from list 1 to list 2
# current_poke_hand = [my_pokemon[2], my_pokemon[5]]
# print(f"Current pokemon: {current_poke_hand}")

# current_poke_hand.insert(1, my_pokemon[3])
# print(f"Current pokemon: {current_poke_hand}")

# # default will remove last item 
# # current_poke_hand.pop()
# # print(f"Current pokemon: {current_poke_hand}")

# # remove specific item at index
# current_poke_hand.pop(0)
# print(f"Current pokemon: {current_poke_hand}")

# 2D

# matrix_list = [[1, 2, 3], ["Darth Maul", "Darth Vader", "Darth Sidius"]]

# temp_list = [
#     [
#         [12], [23]
#     ],
#     [
#         ['cat'], ['dog']
#     ]
# ]

# Grid
# """
# 1  2  3
# DM DV DS

# """ 

# print(f"My favorite person is at position: {matrix_list[0][0]} and they are {matrix_list[1][0]}")

# for i in matrix_list:
#     for j in i:
#         print(j)

# list_example = [expression for item in iterable/structure if condition]

# List Comprehension example
#          0  1  2  3  4
numbers = [2, 4, 6, 8, 10]
squared_values = []

# List comprehension way
# square_values = [x ** 2 for x in numbers]

# Traditional Way
# for x in numbers:
#     squared_values.append(x ** 2)
# print(squared_values)

# can we index the third and forth numbers only
# for pos, x in enumerate(numbers):
#     print(pos, x)
#     if pos == 2:
#         squared_values.append(x ** 2)
#     elif pos == 3:
#         squared_values.append(x ** 2)

# print(squared_values)

# Enumerate 

# list_of_characters = ["sasuke", "ash", "eren", "levi", "guts", "edward", "sanji", "pain", "hamtaro"]

# for-loop
# for name in list_of_characters:
#     print(name)

# # With enumerate
# for count, name in enumerate(list_of_characters):
#     print(f"{count}: {name}")


my_alter_ego = "goku"

print(len(my_alter_ego))


# sort and sorted
# reverse and reversed

# one will alter the list  (sort and reverse)
# create a copy of the list with the new values (sorted and reversed)


# Reverse Example
# Print a list in reverse
# print(f"List: {list_of_characters}")

# # list_of_characters.reverse()

# reversed_list = list(reversed(list_of_characters))

# print(f"List in reverse: {reversed_list}")


# Sort Example

# sorting numbers
# lottery_numbers = [23, 97, 56, 17, 78, 90]

# lottery_numbers.sort(reverse=True)

# print(f"The sorted list is: {lottery_numbers}")

# sorting strings
# list_of_characters = ["sasuke", "ash", "eren", "levi", "guts", "edward elric", "sanji", "pain", "hamtaro"]
# print(f"List before sorted: {list_of_characters}")

# list_of_characters.sort(key=len)

# print(f"The sorted list is: {list_of_characters}")

# copy_of_list_char = sorted(list_of_characters)

# print(f"New Copy of list: {copy_of_list_char}")

# Example of enumerate with dictionary

power_level_dict = {"serge": 9001, "goku": 12, "eren": 89}

for pos, (key, value) in enumerate(power_level_dict.items()):
    print(f"{pos}: Name: {key} : Power Level: {value}")
