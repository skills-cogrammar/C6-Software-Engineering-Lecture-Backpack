# String Basics
my_altar_ego = "Pikachu"
my_other_altar_ego = '^'

# String Concatenation
greeting = "Hallo"
people = "every nyan"

full_greeting = greeting + " " + people
print(full_greeting)

# String formatting
# hallo every nyan, I wish I were a bird

print(f"{greeting} {people}, I wish I were a bird")

# print(greeting + " " + people + ", I wish I were a bird")

# Index and Slicing

# greeting = "H a l l o"
#             0 1 2 3 4  
second_L_in_greeting = greeting[3]
print(second_L_in_greeting)


# Indexing method
second_L_in_greeting_pos = greeting.index("a")
print(f"The position of the letter 'a' in the word {greeting} is: {second_L_in_greeting_pos}.")


index_of_word = people.find("nyan")
print(f"The position of the letter the word 'nyan' in the {people} string is: {index_of_word}.")



# String Methods
"""
- lower()
- upper()
- strip()
- len()
- split()
- join()
- find()
- replace()
- startswith()
- endswith()
"""