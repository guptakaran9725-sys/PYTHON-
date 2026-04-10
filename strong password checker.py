import random
import string

# Function to check password strength
def check_strength(password):
    strength = 0

    # Condition 1: Length
    if len(password) >= 8:
        strength += 1

    # Condition 2: Contains digit
    if any(char.isdigit() for char in password):
        strength += 1

    # Condition 3: Contains uppercase letter
    if any(char.isupper() for char in password):
        strength += 1

    # Condition 4: Contains special character
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength == 4:
        return "Strong 💪"
    elif strength == 3:
        return "Medium 🙂"
    else:
        return "Weak 😢"


# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# Main program
while True:
    print("\n===== Password Tool =====")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        pwd = input("Enter your password: ")
        result = check_strength(pwd)
        print("Password Strength:", result)

    elif choice == "2":
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Length must be greater than 0")
            else:
                new_password = generate_password(length)
                print("Generated Password:", new_password)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        print("Program exited.")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")