"""
MRO = Method Resolution Order [Child, Parent1, Parent2, Parent3]
"""
class Parent1:
    def common_method(self):
        print("Method from Parent1")
        
class Parent2:
    def common_method(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def common_method(self):
        print("Method from Parent2")

# Declare the instance
child_instance = Child()

# Call the common method
child_instance.common_method()

""" =========================
Define a base class and 2 subclasses
"""
class Animal:
    def __init__(self, name:str) -> None:
        self.name = name

    def make_sound(self):
        return f"make generic sound" # Place holder ofr the make_sound method

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: Woof, woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball."

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow, meow."

    def climb_tree(self):
        return f"{self.name} is climbing a tree."
    
# Create instances for Dog and Cat
buddy = Dog("Buddy")
whiskers = Cat("Whiskers")

# Using methods to activate behaviour
print(buddy.make_sound())
print(whiskers.make_sound())

print(buddy.fetch())
print(whiskers.climb_tree())

#Get instances of Dog class
my_dogs = []

# Write function to add an instance
def add_dog(name):
    my_dog = Dog(name)
    my_dogs.append(my_dog)

add_dog("Buddy")
add_dog("Rex")
add_dog("Amber")

total_dogs = len(my_dogs)

dogs_info = [dog.name for dog in my_dogs]
print(dogs_info)        # Output: ['Buddy', 'Rex', 'Amber']

# dogs_info = [dog.name, dog.breed, dog.age for dog in my_dogs]
[['Buddy', 'Lab', 4], 
 ['Rex', 'All Stations', 3], 
 ['Amber', 'Basenji', 2]]