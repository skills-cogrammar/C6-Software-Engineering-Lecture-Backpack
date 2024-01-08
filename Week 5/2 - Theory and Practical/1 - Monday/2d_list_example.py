# example 1

random_numbers = [
    [12, 23, 34],
    [1, 2, 3],
    [10, 20, 30]
]

print(random_numbers[1][1])

# string 2D list
# pet store

cats = ["garfield", "bartholomeow", "tom"]
dogs = ["buster", "big borf", "Mr flapjack"]
birds = ["larry", "sally", "wettle"]

animals = [cats, dogs, birds]

print(animals)  # 2D list

for animal in animals:
    print(f"\n{animal}")
    for pos, i in enumerate(animal, 1):
        print(pos, i)

# dictionary snippet
dict_of_animals = {"cats": cats, "dogs": dogs, "birds": birds}

print(dict_of_animals["cats"][1])

for animal in dict_of_animals:
    print(animal)

# List comprehension examples

# example 1
random_name = "eren jaeger"

# The code is converting each letter in the string `random_name` to uppercase using list
# comprehension. It creates a new list called `converted_name` where each element is the uppercase
# version of each letter in `random_name`. Then, it joins the elements of `converted_name` into a
# single string using the `join()` method with an empty string as the separator. Finally, it prints
# the resulting uppercase string.
converted_name = [letter.upper() for letter in random_name]
print("".join(converted_name))

# # example 2
# The code is creating a new list called `animal_spotter` using list comprehension. It iterates over
# each element in the `list_of_animals` list and creates a new string for each element in the format
# "oh look! a {animal}!". The `{animal}` placeholder is replaced with the current element from
# `list_of_animals`. The resulting strings are added to the `animal_spotter` list. Finally, the
# contents of the `animal_spotter` list are printed.
list_of_animals = ["ant", "mongoose", "hamster", "hyena"]

animal_spotter = [f"oh look! a {animal}!" for animal in list_of_animals]
print(animal_spotter)

# example 3
strange_phrase = "The quick brown fox jumped over the lazy dog"

for x in strange_phrase.split(" "):
    print(x)

# list comprehension way
# The code is using list comprehension to create a new list called `three_worded_words`. It splits the
# string `strange_phrase` into a list of words using the space character as the delimiter. Then, it
# iterates over each word in the list and checks if the length of the word is greater than or equal to
# 5. If the condition is true, the word is added to the `three_worded_words` list. Finally, it prints
# the contents of the `three_worded_words` list.
three_worded_words = [i for i in strange_phrase.split(" ") if len(i) >= 5]
print(three_worded_words)

# # [result/expression | for-loop | condition]


# traditional for-loop way
three_worded_words = []
for word in strange_phrase.split(" "):
    print(word)
    if len(word) == 3:
        three_worded_words.append(word)
print(three_worded_words)


# # value-true if condition else value-false

# The code is assigning the string "Austin Powers" to the variable `rand_word`. Then, it checks if
# `rand_word` is equal to "Austin Powers". If it is, it assigns the string "groovy baby" to the
# variable `is_valid`. If `rand_word` is not equal to "Austin Powers", it assigns the string "not
# groovy baby" to `is_valid`. Finally, it prints the value of `is_valid`, which will be either "groovy
# baby" or "not groovy baby" depending on the value of `rand_word`.
rand_word = "Austin Powers"

is_valid = "groovy baby" if rand_word == "Austin Powers" else "not groovy baby"
print(is_valid)