# PRACTICAL 14: Demonstrating Method Overriding

# Base class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Derived class Dog overrides the sound() method
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof!")

# Derived class Cat overrides the sound() method
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow!")

# Derived class Cow overrides the sound() method
class Cow(Animal):
    def sound(self):
        print("Cow says: Moo Moo!")

# -------------------------------
# Example usage
print("Method Overriding Demonstration:")

animal = Animal()
animal.sound()   # Calls base class method

dog = Dog()
dog.sound()      # Calls overridden method in Dog

cat = Cat()
cat.sound()      # Calls overridden method in Cat

cow = Cow()
cow.sound()      # Calls overridden method in Cow