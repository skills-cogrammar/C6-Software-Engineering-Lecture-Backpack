"""
1. gather ingredients: bread, ham, cheese, lettuce, butter.
2. Take two slices of bread
3. Place butter on both slices
4. Add lettuce
5. Add cheese
6. Put the ham on top
7. repeat process on second slice
8. Put the second slice of bread on top.
9. Press the sandwich toghether.
10. Yu have made the worse sandwich. 
"""

# Gathering ingredients from user and storing in variables
bread_type = input("What type of bread ? [white, brown, rye]")
meat_type = input("What type of meat ? [ham, balony, pastrami, bacon]")
cheese_option = input("Do you want to add cheese ? yes or no")
lettuce_option = input("Do you want to add lettuce ? yes or no")
sauce_option = input("What type of sauce do you want ? [ranch, butter, mayo]")

# printing results or sandwich
# print("Opted for cheese:  " + cheese_option)
# print(f"Opter for lettuce: {lettuce_option}")

print(f"""Your sandwich will be made up of {bread_type} bread 
    with a {meat_type} center, the slices will be sauced up 
    with {sauce_option} with an additional layer of cheese""")
