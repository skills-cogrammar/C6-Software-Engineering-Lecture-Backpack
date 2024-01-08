# creating list
list_of_items = ["shirt", True, 12.3, "mallard", True, "strawberry cake"]

# access elements
second_element = list_of_items[1]
print(second_element)

# modifying elements
list_of_items[2] = "grape"
print(list_of_items)

# add items to the list
list_of_items.append("garry")   # append
print(list_of_items)

list_of_items.insert(2, "squirtle")    # insert
print(list_of_items)

# remove items
list_of_items.remove(True)  # remove function
print(list_of_items)

only_fruit = list_of_items.pop(3) # pop function
print(list_of_items)