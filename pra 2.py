# Python program to demonstrate different operations

# Taking user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Assignment
x = a
print("\nAssignment: x =", x)

# Arithmetic Operations
print("\nArithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

# Relational / Comparison Operations
print("\nRelational / Comparison Operations:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operations
print("\nLogical Operations:")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not(a > b):", not(a > b))

# Bitwise Operations
print("\nBitwise Operations:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("b >> 1:", b >> 1)

# Identity Operations
print("\nIdentity Operations:")
print("a is b:", a is b)
print("a is not b:", a is not b)

# Membership Operations
print("\nMembership Operations:")
numbers = [1, 2, 3, 4, 5, a, b]
print("a in numbers:", a in numbers)
print("b not in numbers:", b not in numbers)