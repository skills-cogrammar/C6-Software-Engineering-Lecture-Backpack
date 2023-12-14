# Example 1

age = 300

if age >= 300:
    print("You are elible to party with the dark side")
else:
    print("Go back to the meditation mountain")


# Example 2
if age > 500:
    print("You are elible to party with the dark side")

elif age >= 300 and age <= 500:
    print("You good to go but wear a helmet")

else:
    print("Go back to the meditation mountain")

# Example 3
jedi_student_grade = 10

if jedi_student_grade >= 90:
    print("A Grade")

elif jedi_student_grade >= 80:
    print("B Grade")

elif jedi_student_grade >= 70:
    print("C Grade")

elif jedi_student_grade >= 60:
    print("D Grade")
else:
    print("Fail")


# Example 4
is_weather_gloomy = True
is_feeling_darkside = True

if is_weather_gloomy:
    if is_feeling_darkside:
        print("Maybe take a nap")
    else:
        print("Proceed with meditation")
else:
    print("Go try to get into the club again")
    