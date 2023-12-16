"""
Marathon Medals Program
"""

"""
1. Get user time through input() statement as integer  
2. Create constants to represent time ranges
3. Create variable to store medal awarded
4. Create conditional structure to determine user medal
5. return response to user based of time achieved
6. Close off program
"""

# Grabbing user time
user_time = int(input("Marathon time was it? "))

# Adding medal constant ranges
gold_medal_time = 10
silver_medal_time = 15
bronze_medal_time = 20
completion_medal_limit = 50

# Creating medal variable
user_medal = ""

# Conditional body to determine reward
if user_time <= gold_medal_time or user_time < silver_medal_time:
    user_medal = "Gold"
elif user_time >= silver_medal_time and user_time < bronze_medal_time:
    user_medal = "Silver"
elif user_time >= bronze_medal_time and user_time < completion_medal_limit:
    user_medal = "Bronze"
else:
    user_medal = "Completion"

# Returning result to user
print(f"""You completed the race in: {user_time} minutes
            {user_medal} medal You have gotten!""")
