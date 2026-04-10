# PRACTICAL 16: Demonstrating Data Hiding

class Student:
    def __init__(self, name, age, marks):
        self.name = name              # public attribute
        self._age = age               # protected attribute (convention)
        self.__marks = marks          # private attribute (name mangling)

    # Public method to access private data
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Marks:", self.__marks)

    # Getter method for private attribute
    def get_marks(self):
        return self.__marks

    # Setter method for private attribute
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")


# -------------------------------
# Example usage
student1 = Student("Vahib", 21, 85)

# Accessing public method
student1.show_details()

# Accessing protected attribute (possible but discouraged)
print("\nAccessing protected attribute _age directly:", student1._age)

# Accessing private attribute directly (will cause error)
# print(student1.__marks)   # Uncommenting this will raise AttributeError

# Accessing private attribute using getter
print("Marks (via getter):", student1.get_marks())

# Updating private attribute using setter
student1.set_marks(92)
print("Updated Marks (via getter):", student1.get_marks())

# Trying to set invalid marks
student1.set_marks(150)