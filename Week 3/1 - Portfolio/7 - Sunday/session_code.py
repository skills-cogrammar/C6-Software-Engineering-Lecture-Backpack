# Menu Base with Try/Except 
store_items = ["house", "eldritch horror", "dragon"]

while True:
    print("Menu: ")
    print("1. Add Pokemon ")
    print("2. Check on Pokemon ") 
    print("3. Call on Pokemon ")
    print("4. Quit ")

    try:
        user_input = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input. Please enter a number.")
    else:
        if user_input == 1:
            print("Performing first option")
        elif user_input == 2:
            print("Performing second option")
            for pos, item in enumerate(store_items, 1):
                print(f"Item{pos}: {item}")
                
            try:
                user_item = int(input("Pick Item number: "))
                user_item_pos = store_items[user_input - 1]
                print(f"You have picked the: {user_item_pos}")
            except IndexError:
                print("Item is not in list")

        elif user_input == 3:
            print("Performing third action")
        elif user_input == 4:
            print("Thank you for using Pokemon UI!")
            break
        else:
            print("Pick an option from the menu!")

# KeyBoardInterupt
# try:
#     while True:
#         print("Menu: ")
#         print("1. Add Pokemon ")
#         print("2. Check on Pokemon ") 
#         print("3. Call on Pokemon ")
#         print("4. Quit ")

#         user_input = input("Enter something to stop loop: (Ctrl+C to exit): ")
#         print(f"Ohhhhh noooo, you have entered {user_input}")
# except KeyboardInterrupt:
#     print("\n You have forcefully shutdown the program! ")
