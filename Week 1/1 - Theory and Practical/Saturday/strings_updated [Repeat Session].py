# Variable Declaration
name = "Peter"
surname = "Parker"

full_name = name + " " + surname
print(full_name)

random_sentence = f"{name} you are not the father! Your surname isn't {surname}"
print(random_sentence)

# String Methods
## Len()
unknown_billion_guy = "batman"

print(f"The length of the unknown guys name is: {len(unknown_billion_guy)}")

password_valid = input("Enter a password: ")

if len(password_valid) >= 6:
    print("This is a strong password")
else:
    print("Your password is weak said Dumbledore calmly!")

## Upper() and Lower()
name = "luke"
evil_dad = "darth"

message = f"{name.capitalize()}, I aM yoUr Father! {evil_dad.capitalize()}"

print(message)

# # Strip()
message = "****They've****taken****the****hobbits****to****Eisengaurd!!****"
# print(message.strip("*"))

message = message.strip("*").replace("*", " ").replace("    ", " ")
print(message)

## Split 
message = "Levi is better than Eren Jaegar"

message_split = message.split()
print(message_split)

prank_message = f"{message_split[4]} is better than {message_split[0]}"
print(prank_message)

# Join()
list_of_words = ["***", "I", "want", "to", "be", "the","very", "best", "that", "no", "one", "ever", "was"]

combined_words = " ".join(list_of_words)

print(combined_words)

combined_words_updated = combined_words.strip("*")
print(combined_words_updated)
