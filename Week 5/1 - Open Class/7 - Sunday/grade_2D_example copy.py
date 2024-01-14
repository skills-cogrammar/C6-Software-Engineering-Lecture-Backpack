from tabulate import tabulate
# Grade 2D List

# Grades - field work, combat, Maths
poke_grade_list = [
    ["Pokemon Name", "Field Work", "Combat", "Maths"],
    ["Pikachu", 85, 83, 56],
    ["Squirtle", 90, 75, 70],
    ["Psyduck", 70, 50, 97]
]

poke_grade_list.append(["Charizard", 45, 89, 69])


# Representing through tabulate method
new_poke_grade_list = tabulate(poke_grade_list, headers='firstrow', tablefmt='grid')
print(new_poke_grade_list)

# accessing combat grades
# pikachu_combat_grade = poke_grade_list[0][2]
# psyduck_combat_grade = poke_grade_list[2][2]

# print(f"""{poke_grade_list[0][0]} has scored a combat
#       grade of: {pikachu_combat_grade}""")

# print(f"""{poke_grade_list[2][0]} has scored a combat
#       grade of: {psyduck_combat_grade}""")

# display their maths grades
# for poke_stat in range(len(poke_grade_list)):
#     poke_name = poke_grade_list[poke_stat][0]
#     for poke in range(len(poke_grade_list[poke_stat])):
#         # Challenge Print out each of our pokemons grade
#         if poke == 1:
#             field_work_grade = poke_grade_list[poke_stat][poke]
#         elif poke == 2:
#             combat_grade = poke_grade_list[poke_stat][poke]
#         elif poke == 3:
#             maths_grade = poke_grade_list[poke_stat][poke]

#     print(f"\n{poke_name}'s grades: \nField Work: {field_work_grade} \nCombat: {combat_grade} \nMaths: {maths_grade}")
