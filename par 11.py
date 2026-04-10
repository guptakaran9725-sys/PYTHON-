# PRACTICAL 11: Employee Class with Inheritance

# Base class
class Employee:
    def __init__(self):
        self.emp_name = ""
        self.emp_age = 0
        self.emp_city = ""

    # Method to take user input
    def get_data(self):
        self.emp_name = input("Enter Employee Name: ")
        self.emp_age = int(input("Enter Employee Age: "))
        self.emp_city = input("Enter Employee City: ")

# Derived class
class Emp_Derived(Employee):
    def __init__(self):
        # Call get_data() from base class
        super().get_data()
        # Display attributes upon instantiation
        print("\nEmployee Details:")
        print("Name:", self.emp_name)
        print("Age:", self.emp_age)
        print("City:", self.emp_city)


# -------------------------------
# Example usage
emp = Emp_Derived()