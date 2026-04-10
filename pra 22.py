# PRACTICAL 22: Importing Different Packages

# Importing math package
import math

# Importing random package
import random

# Importing datetime package
import datetime

# Importing os package
import os

# Importing sys package
import sys


# -------------------------------
# Example usage

print("Using math package:")
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

print("\nUsing random package:")
print("Random number between 1 and 100:", random.randint(1, 100))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

print("\nUsing datetime package:")
current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)

print("\nUsing os package:")
print("Current Working Directory:", os.getcwd())

print("\nUsing sys package:")
print("Python Version:", sys.version)