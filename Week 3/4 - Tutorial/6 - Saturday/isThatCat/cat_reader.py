# create a program to read a list of cats

# opening file
with open("list_of_cats.txt", "r") as file:
    content = file.readlines()

for cat in content:
    cat_name = cat.strip("\n")
    print(f"I can confirm that {cat_name} is a cat!")
    