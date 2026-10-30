# Creating a Dog class
class Dog:

    # Constructor: initializes the object's attributes
    def __init__(self, dog_name, dog_color, dog_age):

        self.__dog_name = dog_name  # Private variable (double underscore)
        self.dog_color = dog_color  # Public variable (no underscore)
        self._dog_age = dog_age     # Protected variable (single underscore)


# Creating an object of the Dog class
dog1 = Dog("Tommy", "Black", 5)


# -----------------------------------
# Accessing Public, Protected and Private Variables
# -----------------------------------

# Accessing private variable using Name Mangling
# Python internally changes __dog_name to _Dog__dog_name
print(dog1._Dog__dog_name)  # Output: Tommy

# Accessing public variable directly
print(dog1.dog_color)       # Output: Black

# Accessing protected variable directly
# Protected variables can also be accessed outside the class in Python
print(dog1._dog_age)        # Output: 5


# -----------------------------------
# Modifying Private Variable using Name Mangling
# -----------------------------------

# Changing the private variable using its mangled name
dog1._Dog__dog_name = "Max"

# Displaying the updated private variable
print(dog1._Dog__dog_name)  # Output: Max