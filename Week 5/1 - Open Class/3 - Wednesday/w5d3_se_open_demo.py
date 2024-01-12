# Normal code for creating number list for range(1, 6)
num_list = []

for iteration in range(1, 6):
    num_list.append(iteration)
    print(num_list)

# Let's now use List Comprehension
num_list = [iteration * 2 for iteration in range(1, 6)]
print(f"List comp: {num_list}")

# Another option
num_list = list(range(1, 6))
print(f"Casting: {num_list}")

# ---- Complex list comprehension
# Normal code
result = []
for x in range(10):                 # my_range = [0,1,2,3,4,5,6,7,8,9]
    if x > 2 and x < 8:             # [3,4,5,6,7]
        if x % 2 == 0:              # Test for even number
            result.append(x ** 2)
        else: 
            result.append(0)
        
print(f"result: {result}")          # result = [0, 16, 0, 36, 0]

# Complex comprehension
complex_squares = [x ** 2 if x % 2 == 0 else 0 for x in range(10) if x > 2 and x < 8]
print(f"complex: {complex_squares}") 

# ==============  How to iterate over a List and a dictionary.
clothing_prices = {"Shoes": 12,
                    "Dress" : 30,
                    "Shirt": 20,
                    "Pants" : 20,
                    "Socks" : 5}

dress_items = ["Dress", "Shoes"] 
pants_items = ["Pants", "Shirt", "Shoes", "Socks"]

# Dress Code
dress_set = ''
total_dress_cost = 0

for item in dress_items:
    dress_set += item + "\n"
    total_dress_cost += clothing_prices[item]     # dictionary key in [] and not {}

print("==== Summary of Dress Compilation ====\n")
pound_symbol = chr(163)
print(f"{dress_set}\nThe total for the above items are : " 
      f"{pound_symbol}{total_dress_cost:.2f}")

# Pants code
pants_set = ""
total_pants_cost = 0

for item in pants_items:
    pants_set += item + "\n"
    total_pants_cost += clothing_prices[item]  

print("\n==== Summary of Pants Compilation ====\n")
print(f"{pants_set}\nThe total for the above items are : " 
      f"{pound_symbol}{total_pants_cost:.2f}")

# ============  Additional   Examples
# ------------------------------------
# Conditional Expression (or Ternary Operator)
x = 4

# --- Normal code
if (x == 5):
    print("Because the condition is true")
else:
    print("Because the condition is false")

            # True                          | condition     | False
result = "Because the condition is true" if x == 5 else "Because the condition is false"
print(result)

# ------------------------------------
# More More More - Conditional Expression (or Ternary Operator)

# --- Determining the maximum of two numbers
num1 =  5
num2 = 11
max_value = num1 if num1 > num2 else num2

# *** Challenge: Write the normal code for above

# --- if:elif - Checking if a number is positive, negative, or zero
num = -3
status = "positive" if num > 0 else ("negative" if num < 0 else "zero")

# *** Challenge: Write the normal code for above

# --- Categorizing a person's age group
age = 99
age_group = "child" if age < 12 else ("teen" if age < 18 else "adult")

# *** Challenge: Write the normal code for above

