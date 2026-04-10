# Python program to demonstrate basic string methods

text = "  Hello World! Python is FUN.  "

print("Original String:", repr(text))

# lower()
print("\nLowercase:", text.lower())

# islower()
print("Is Lowercase?:", text.islower())

# upper()
print("\nUppercase:", text.upper())

# isupper()
print("Is Uppercase?:", text.isupper())

# join()
words = ["Python", "is", "awesome"]
print("\nJoin with space:", " ".join(words))

# split()
print("Split by space:", text.split())

# find()
print("\nFind 'Python':", text.find("Python"))

# replace()
print("Replace 'FUN' with 'powerful':", text.replace("FUN", "powerful"))

# strip()
print("\nStrip spaces:", text.strip())

# title()
print("Title Case:", text.title())

# swapcase()
print("Swapcase:", text.swapcase())

# capitalize()
print("Capitalize:", text.capitalize())

# casefold()
print("Casefold (stronger lower):", text.casefold())

# format()
name = "Vahib"
age = 25
print("\nFormat Example:", "My name is {} and I am {} years old.".format(name, age))