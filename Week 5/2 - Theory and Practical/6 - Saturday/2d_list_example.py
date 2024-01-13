# example 1

random_numbers = [
    [12, 23, 34],
    [1, 2, 3],
    [10, 20, 30]
]

# element = grid[row_index][column_index]
random_num_from_grid = random_numbers[2][1]

print(random_num_from_grid)

# Iterating through 2D List
for item in random_numbers:
    print(item)
    for sub_item in item:
        print(sub_item)

# string 2D list
# pet store

# cats = ["garfield", "bartholomeow", "tom"]
# dogs = ["buster", "big borf", "Mr flapjack"]
# birds = ["larry", "sally", "wettle"]

# animals = [cats, dogs, birds]

# print(animals)  # 2D list

# for animal in animals:
#     print(f"\n{animal}")
#     for pos, i in enumerate(animal, 1):
#         print(pos, i)

# dictionary snippet
# dict_of_animals = {"cats": cats, "dogs": dogs, "birds": birds}

# print(dict_of_animals["cats"][1])

# for animal in dict_of_animals:
#     print(animal)

# List comprehension examples

# example 1
# random_name = "eren jaeger"

# converted_name = [letter.upper() for letter in random_name]
# print("".join(converted_name))

# # example 2
# list_of_animals = ["ant", "mongoose", "hamster", "hyena"]

# animal_spotter = [f"oh look! a {animal}!" for animal in list_of_animals]
# print(animal_spotter)

# example 3
# strange_phrase = "The quick brown fox jumped over the lazy dog"

# for x in strange_phrase.split(" "):
#     print(x)

# list comprehension way
# three_worded_words = [i for i in strange_phrase.split(" ") if len(i) >= 5]
# print(three_worded_words)

# # [result/expression | for-loop | condition]


# traditional for-loop way
# three_worded_words = []
# for word in strange_phrase.split(" "):
#     print(word)
#     if len(word) == 3:
#         three_worded_words.append(word)
# print(three_worded_words)


# # value-true if condition else value-false

# rand_word = "Austin Powers"

# is_valid = "groovy baby" if rand_word == "Austin Powers" else "not groovy baby"
# print(is_valid)
