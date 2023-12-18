"""FOR LOOPS"""

# Example 1: Range function, will loop over a sequence of numbers
for num in range(0, 3):
    print(num)
    num = 66
    print(num)

# Example 2: Iterate over a list of items or stuff
list_wizards = ["Dumbledore", "Gandalf", "Saruman", "Palpatine", "Merlin", "Radagast"]
for wizard in list_wizards:
    print(f"{wizard} is a wizard!")

# Example 3: Calculate sum of value using range()
total = 0

for number in range(1, 6):
    print(f"The current value of number is: {number}")
    print(f"The current total is: {total}")
    total += number
print(f"Sum: {total}")

# Example 4: Enumerate()
pokemons = ["metapod", "pikachu", "charmeleon",
            "charizard", "charmander", "serge",
            "snorlax", "wartotle", "magikarp"]
# index = 0

# for poke in pokemons:
#     print(index, poke)
#     index += 1

# Enumerate()
total = 0
for pos, poke in enumerate(pokemons, 1):
    print(pos, poke)
    total += 1

print(pos)
# Count: The count of the current iteration
# Poke: The value of the item at current iteration

# Example 5: Break

# print(pokemons[1])
for pos, poke in enumerate(pokemons, 1):
    if poke == "pikachu":
        print(f"Pikachu is in position {pos}!")
        break

# Example 6: Continue

# print(pokemons[1])

for pos, poke in enumerate(pokemons, 1):
    if poke in ["charmeleon", "charizard", "charmander"]:
        print(f"{poke} You are fire type!")
    else:
        print(f"{poke} you are different type!")
