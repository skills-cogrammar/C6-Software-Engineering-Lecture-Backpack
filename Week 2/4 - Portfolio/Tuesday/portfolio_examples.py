# Using Lists
list_of_items = ["Orange"]

list_of_items.append("Banana")
list_of_items.append("Apple")
list_of_items.append("Chair")
list_of_items.append("Pear")

# # printing out list of items
# print(list_of_items)

# # Removing the element
# remove_item = "Chair"
# list_of_items.remove(remove_item)

# print(list_of_items)

# Displaying using a while loop
# done = False
# counter = 0

# while (not done):
#     if (counter == len(list_of_items) - 1):
#         done = True
#     print("Item {:2}:  \t{}".format(counter+1, list_of_items[counter]))
#     counter += 1

# Displaying using a for loop
# for counter, item in enumerate(list_of_items, 1):
#     print(f"Item {counter}: \t{item}")

# Create atm menu
done = False

while (not done):
    print("\n")
    print("1 - Check balance")
    print("2 - Withdraw")
    print("3 - Deposit")
    print("4 - Exit (Return Card)")
    user_input = int(input("Enter your choice: "))

    if user_input == 1:

        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        done = True
    else:
        print("Invalid option picked, try again!!!!!")
