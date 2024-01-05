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
numbers = [2, 4, 6, 8, 10]

square_values = [x ** 2 for x in numbers]
print(square_values)