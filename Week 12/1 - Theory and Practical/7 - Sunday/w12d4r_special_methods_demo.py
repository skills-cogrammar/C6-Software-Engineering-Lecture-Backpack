# Declare class with special methods __init__, __str__ and __repr__
class Laptop:
    def __init__(self, brand:str, serial_number:str, screen_size:str) -> None:
        self.brand = brand
        self.serial_number = serial_number
        self.screen_size = screen_size

    def __str__(self) -> str:
        str_rep = f"Brand: {self.brand}\nSerial: {self.serial_number}\n" \
                    f"Screen Size: {self.screen_size}\n"
        return str_rep
    
    def __repr__(self) -> str:
        return f"Laptop({self.brand}, {self.serial_number}, {self.screen_size})"
    
# == Main Code
laptop = Laptop("Asus", "ASHDB123", "17")
str_laptop = str(laptop)
print(str_laptop)

# ==============================
# Declare class with special methods __init__, __str__ and __add__
class MyNumber:
    def __init__(self, value) -> None:
        self.value = value 

    def __str__(self) -> str:
        return str(self.value)

    def __add__(self, other):
        return MyNumber(self.value + other.value)
    
# === Main Code
# Create instances
num1 = MyNumber(25)
num2 = MyNumber(14)

num3 = num1 + num2  # Python uses the __add__() special method
print(num1)
print(num2)
print(num3)

# ========================
# Declare class with method & special methods __init__, get_area, __add__ & __sub__
class Rectangle:
    def __init__(self, width1, length1) -> None:
        self._width = width1
        self._length = length1

    def get_area(self):
        return self._width * self._length
    
    def __add__(self, other):
        width = self._width + other._width
        length = self._length + other._length
        
        return Rectangle(width, length)
    
    def __sub__(self, other):
        width = self._width - other._width
        length = self._length - other._length
        
        return Rectangle(width, length)
    
# ===== Main Code
# Create instances
rect1 = Rectangle(6, 11)
rect2 = Rectangle(3, 7)
rect3 = rect1 - rect2

"""
----------------
|  rect3 area   |
|       --------|
|      |        |
|      |        |
----------------
"""

print(rect3.get_area())

# =====================
# Declare class with method & special methods __init__, getitem, __len__ & __contains__
class ContactList:
    def __init__(self) -> None:
        self.contant_list = []

    def add_contant(self, contact):
        self.contant_list.append(contact)

    def __getitem__(self, key):
        return self.contant_list[key]
    
    def __len__(self):
        return len(self.contant_list)
    
    def __contains__(self, item):
        for contact in self.contact_list:
            if contact.name == item:
                return True
            
        return False
    
class Contact:
    def __init__(self, name) -> None:
        self.name = name

    # To solve the memory display in print(contact_list[1]), we need a 
    # __str__ method for the Contact class
    
    def __str__(self):
        return f"Contact: {self.name}"
    
# ==== Main Code
# Create instances
contact_list = ContactList()

contact_list.add_contant(Contact("James"))
contact_list.add_contant(Contact("Joe"))

"""
Remember the __str__ print method to print this correctly.
We cannot use print(str(contact_list[1])) if there is not __str__ to call.
We also do not have a __repr__ method of our own as default for __str__ and
therefore Python will go to its own default __repr__ during runtime. 
This is the __repr__ that will display the developers view with the memory address.
"""
print(contact_list[1])   # This is using the __getitem__ special method

if "James" in contact_list:  # This is using the __contains__ special method
    print("James had enough of this session now!")
