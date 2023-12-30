# calculate discount of item

# add try/catch
while True:
    try:
        item_original_price = int(input("Enter item price: "))
        discount_percentage = int(input("Enter discount amount: "))

    # except TypeError:
    #     print("The type you have entered does match")
    except ValueError:
        print("Make sure to enter price only")
    else:
        break


discount_percentage = input("Enter discount amount: ")
if discount_percentage.isdigit():
    print("awesome, NOICE!")
else:
    print("enter a number!")


# price after discount calculation
item_discounted_price = item_original_price * (1 - discount_percentage / 100)

# discount price
updated_item_discounted_price = item_original_price - item_discounted_price

print(f"The discounted price: {updated_item_discounted_price}")
print(f"The current item price is: {item_discounted_price}")
