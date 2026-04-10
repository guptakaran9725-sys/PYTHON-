# PRACTICAL 17: Exception Handling in Python

# I. try-except (try-catch) block
def demo_try_except():
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Error: Invalid input! Please enter an integer.")

# II. Raising an exception using raise keyword
def demo_raise():
    age = int(input("\nEnter your age: "))
    if age < 18:
        raise Exception("Age must be 18 or above to proceed.")
    else:
        print("Access granted!")

# III. try-finally block
def demo_try_finally():
    try:
        num1 = int(input("\nEnter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
        print("Result:", result)
    finally:
        print("Execution of try-finally block completed (cleanup code runs here).")


# -------------------------------
# Example usage
print("I. Demonstrating try-except:")
demo_try_except()

print("\nII. Demonstrating raise keyword:")
try:
    demo_raise()
except Exception as e:
    print("Caught Exception:", e)

print("\nIII. Demonstrating try-finally:")
demo_try_finally()