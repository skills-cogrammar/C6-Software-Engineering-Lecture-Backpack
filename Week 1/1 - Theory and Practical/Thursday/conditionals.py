# Example 1: Basic if statement
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote yet.")


# Example 2: if-elif-else chain
grade = 75

if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")
else:
    print("You need improvement.")


# Example 4: Nested if statements
is_weekend = True
is_sunny = False

if is_weekend:
    if is_sunny:
        print("Go for a picnic!")
    else:
        print("Relax at home.")
else:
    print("It's a weekday, focus on work or study.")