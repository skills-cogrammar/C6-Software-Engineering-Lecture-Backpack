# Grade 2D List

# Grades - field work, combat, Maths
poke_grade_list = [
    ["Pikachu", 85, 83, 56],
    ["Squirtle", 90, 75, 70],
    ["Psyduck", 70, 50, 97]
]

# accessing combat grades
# pikachu_combat_grade = poke_grade_list[0][2]
# psyduck_combat_grade = poke_grade_list[2][2]

# print(f"""{poke_grade_list[0][0]} has scored a combat
#       grade of: {pikachu_combat_grade}""")

# print(f"""{poke_grade_list[2][0]} has scored a combat
#       grade of: {psyduck_combat_grade}""")

# display their maths grades
for poke_stat in range(len(poke_grade_list)):
    poke_name = poke_grade_list[poke_stat][0]
    for poke in range(len(poke_grade_list[poke_stat])):
        # Challenge Print out each of our pokemons grade
