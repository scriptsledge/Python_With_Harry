# Base class for all animals
class Animals:
    pass

# Subclass of Animals for pets
class Pets(Animals):
    pass

# Subclass of Pets for dogs
class Dog(Pets):
    """
    Represents a dog with a bark method.
    """

    @staticmethod
    def bark():
        """
        Prints a dog's bark sound.
        """
        print("Bhow Bhowww, bhow-bow-bow!!!")

# Create an instance of Dog and call its bark method
tom = Dog()
tom.bark()