""" =========================
Using super() function for single inheritance
"""
# ==============  Declare Class Types 
class Animal:
    def __init__(self, species:str, name:str) -> None:
        self._species = species
        self._name = name

    def make_sound(self):
        return f"make generic sound" # Place holder for the make_sound method

    def get_species_description(self):
        return f"{self._name} is a {self._species}" 

    def __str__(self) -> str:
        return f"{self._species} {self._name}"

class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__("Dog", name)

        self._breed = breed

    def make_sound(self):
        return f"{self._name} barks: Woof, woof!"

    def get_description(self):
        return super().get_species_description() + f" and a {self._breed} breed" 
    
    def __str__(self) -> str:
        return f"{self._name} is a {self._breed} {self._species}"

class Cat(Animal):
    def __init__(self, name: str, colour: str) -> None:
        super().__init__("Cat", name)

        self._colour = colour

    def make_sound(self):
        return f"{self._name} meows: Meow, meow."

    def get_description(self):
        return super().get_species_description() + f" with {self._colour} fur" 
    
    def __str__(self) -> str:
        return f"{self._name} is a {self._colour} {self._species}"
    
# ============  Declare functions
# Write function to add an instance
def add_dog(name, breed):
    dog_instance = Dog("Rover", "Golden Retriever")
    my_dogs.append(dog_instance)

    return dog_instance

# ===========  Main Code
my_dogs = []
# Create instances for Dog and Cat
new_dog = add_dog("Rover", "Golden Retriever")

cat_instance = Cat("Tom", "Tabby")

# Using methods to activate behaviour
print(new_dog.make_sound())
print(cat_instance.make_sound())
print(f"{'=' * 30}")

print(new_dog.get_description())
print(cat_instance.get_description())
print(f"{'=' * 30}")

# Using isinstance() and issubclass()
print(f"{new_dog} an instance of Animal: ", isinstance(new_dog, Animal))
print(f"{new_dog} an instance of Dog: ", isinstance(new_dog, Dog))
print(f"{new_dog} an instance of Cat: ", isinstance(new_dog, Cat))

print(f"{cat_instance} an instance of Animal: ", isinstance(cat_instance, Animal))
print(f"{cat_instance} an instance of Dog: ", isinstance(cat_instance, Dog))
print(f"{cat_instance} an instance of Cat: ", isinstance(cat_instance, Cat))


#===========================  SHAPES    ===========================
# ============ Import libraries


# ============ Declare Class Types
# How can isinstance and issubclass help us in the logic of code
class Shape:
    def __init__(self, colour) -> None:
        self.colour = colour

    def area(self):
        raise NotImplementedError("Subclass must implement the area method")
    
class Circle(Shape):
    def __init__(self, colour, radius) -> None:
        super().__init__(colour)

        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
    def __str__(self):
        return "Circle"

class Rectangle(Shape):
    def __init__(self, colour, width, length) -> None:
        super().__init__(colour)

        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
    def __str__(self):
        return "Rectangle"
    
# ============ Declare functions
def calculate_total_area(shapes):
    total_area = 0

    for shape in shapes:
        # Check if the current object is an instance of the Shape Class
        # if isinstance(shape, Shape) == True:
        if issubclass(shape.__class__, Shape) == True:
            total_area += shape.area()
            print(f"Valid shape: {shape}")
        else:
            print(f"Skipping invalid shape: {shape}")

    return total_area

# ============ Main Code
#Create instances of the shapes
circle_instance = Circle("Red", 5)
rectangle_instance = Rectangle("Blue", 4, 6)
invalid_shape = "Invalid Shape"

# Calculate the total_area from the list
shapes_list = [circle_instance, rectangle_instance, invalid_shape]

total_area_out = calculate_total_area(shapes_list)
print(f"Total Area of shapes: {total_area_out}")

#===========================  BATS    ===========================
"""
Using super() function for double inheritance of subclasses
"""
class Animal:
    def __init__(self, species: str = "") -> None:
        self.species = species

    def make_sound(self):
        return f"The {self.species} makes a generic sound."

class Mammal(Animal):
    def __init__(self, fur_colour: str, species: str = "Mammal") -> None:
        super().__init__(species)  
        self.fur_colour = fur_colour
        
    def show_colour(self):
        return f"The {self.species} is a {self.fur_colour} colour."
    
    def give_birth(self):
        return f"The {self.species} gives birth to live young."

class Bird(Animal):
    def __init__(self, beak_type: str, species: str = "Bird") -> None:
        super().__init__(species)
        self.beak_type = beak_type
    
    def fly(self):
        return f"The {self.species} is flying with its {self.beak_type} beak."

class Amphibian(Animal):
    def __init__(self, skin_type: str, species: str = "Amphibian", ) -> None:
        super().__init__(species)

        self.skin_type = skin_type

    def jump(self):
        return f"The {self.species} jumps with it's {self.skin_type} skin."
    
class Bat(Mammal, Bird):
    def __init__(self, fur_colour: str, beak_type: str, species: str = "Bat") -> None:
        # Use super() to call constructors of parent classes
        Mammal.__init__(self, fur_colour, species)
        Bird.__init__(self, beak_type, species)

    def echolocate(self):
        return f"The {self.species} is using echolocation."

# ============ Main Code
# Create instances
mammal_instance = Mammal("golden", "Lion")
bird_instance = Bird("hooked", "Eagle")
amphibian_instance = Amphibian("smooth", "Frog")
bat_instance = Bat("brown", "sharp", "Bat")

# Display information about animals
print(mammal_instance.make_sound())
print(mammal_instance.show_colour())
print(mammal_instance.give_birth())
print("===============")

print(bird_instance.make_sound())
print(bird_instance.fly())
print("===============")

print(amphibian_instance.make_sound())
print(amphibian_instance.jump())
print("===============")

print(bat_instance.make_sound())
print(bat_instance.echolocate())
print("===============")
