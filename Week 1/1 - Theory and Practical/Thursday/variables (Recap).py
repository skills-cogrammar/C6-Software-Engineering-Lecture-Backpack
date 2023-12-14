warrior_name = "General Kenobi"
num_var = 34
float_var = 12.4
force_wiedling = False
force_or_nah = "maybe"


# Conditional Check
if force_wiedling:
    print("you are Jedi Warrior")
elif force_or_nah == "maybe":
    print("""You may be force sensitive, please meditate and find a really 
          high mountain top to look over gloomingly""")
else:
    print("You are but a normal person")

jedi_life_span = 800

if jedi_life_span >= 100 and jedi_life_span <= 300 and force_or_nah == "maybe":
    print("You lived a short life")

if jedi_life_span >= 100:
    if jedi_life_span <= 300:
        print("You have lived a short life")
