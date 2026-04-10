# PRACTICAL 10: User-defined functions

# Function with a single argument
def greet(name):
    print("Hello,", name)

# Function with multiple arguments
def add_numbers(a, b):
    return a + b

# Function with arbitrary arguments (*args)
def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Demonstration
print("Single Argument Function:")
greet("Vahib")

print("\nMultiple Arguments Function:")
print("Sum of 10 and 20:", add_numbers(10, 20))

print("\nArbitrary Arguments Function:")
print("Multiplication of 2, 3, 4:", multiply_numbers(2, 3, 4))


# -------------------------------
# Simple Calculator using user-defined functions

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

# Example usage
print("\nSimple Calculator:")
num1 = 15
num2 = 3
print("Addition:", calculator(num1, num2, "add"))
print("Subtraction:", calculator(num1, num2, "subtract"))
print("Multiplication:", calculator(num1, num2, "multiply"))
print("Division:", calculator(num1, num2, "divide"))