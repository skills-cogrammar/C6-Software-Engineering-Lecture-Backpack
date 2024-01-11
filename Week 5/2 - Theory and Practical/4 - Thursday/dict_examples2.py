# Example 1

# jedi_info = {
#     'name': "Obi Wan",
#     'age': 66,
#     'rank': "Jedi Master",
#     'skills': ["charisma", "ninja step",
#                "force wielding", "maths", "physics", "baking"],
#     'address': {
#         'street': '123 Main St',
#         'city': 'Paris',
#         'zipcode': 122334
#     },
#     'is_strong': True
# }

# # first loop
# # for key, value in jedi_info.items():
# #     print(key, value)

# # print(jedi_info["skills"])
# # jedi_skills = jedi_info["skills"]

# # second loop
# for key, value in jedi_info.items():
#     if key == "skills":
#         for skill in value:
#             print(skill)

# Example 2
# favorite_movies = {
#     'action': ["John Wick", "Spongebob", "Kingsmen"],
#     'drama': ["Forrest Gump", "Titanic", "Twilight"],
#     'confusing': ["inception", "tennet", "interstellar"],
#     "comedy": ["Borat", "Mr bean", "Die Hard", "Monty Python"]
# }

# for pos, key in enumerate(favorite_movies.keys()):
#     print(f"{pos}: {key}")

# user_input = input("What type of genre do you feel like tonight: enter genre ").lower()

# user_chosen_genre = favorite_movies[user_input]

# print("Available Movies: ")
# for movie in user_chosen_genre:
#     print(movie)

# Example 3
weather_data = {
    'temperature': 25,
    'conditions': "Sunny",
    'forecast': ["Clear", "Partly Cloudy", "Sunny", "Clear"]
}

# # Check if it's hot day
if weather_data['temperature'] > 30:
    # weather_data.update({'hot_day': True})
    weather_data['hot_day'] = True
else:
    weather_data['hot_day'] = False

print(weather_data)


# Example 4
favorite_movies = {
    'Inception': {'rating': 9.0, 'genre':'confusing'},
    'The royal Tenenbaums': {'rating': 8.6, 'genre': 'comedy'},
    'Spongebob Movie': {'rating': 10, 'genre': 'action'}
}

# The line `my_top_films = [title for title, data in favorite_movies.items() if data['rating'] > 9]`
# is creating a list called `my_top_films` that contains the titles of movies from the
# `favorite_movies` dictionary where the rating is greater than 9.
my_top_films = [title for title, data in favorite_movies.items() if data['rating'] > 9]

print(my_top_films)