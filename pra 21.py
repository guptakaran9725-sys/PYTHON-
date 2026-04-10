# PRACTICAL 21: Create 26 text files (A.txt to Z.txt)

import string

def create_files():
    for letter in string.ascii_uppercase:   # 'A' to 'Z'
        filename = f"{letter}.txt"
        with open(filename, "w") as file:
            file.write(f"This is file {filename}\n")
        print(f"Created: {filename}")

# -------------------------------
# Example usage
create_files()