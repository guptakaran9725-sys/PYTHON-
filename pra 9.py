# PRACTICAL 9: Pattern Printing

# a. Number triangle (1, 1 2, 1 2 3, ...)
print("Pattern a:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# b. Continuous numbers triangle (1, 2 3, 4 5 6, ...)
print("\nPattern b:")
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# c. Star triangle (*, * *, * * *, ...)
print("\nPattern c:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# d. Alphabet triangle (A, B B, C C C, ...)
print("\nPattern d:")
ch = 65  # ASCII value of 'A'
for i in range(1, 6):
    for j in range(i):
        print(chr(ch), end=" ")
    ch += 1
    print()