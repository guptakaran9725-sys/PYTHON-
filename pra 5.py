# PRACTICAL 5: Demonstrating Python Tuple operations

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50, 20, 30)
print("Original Tuple:", my_tuple)

# count()
print("\nCount of 20:", my_tuple.count(20))
print("Count of 30:", my_tuple.count(30))

# index()
print("Index of 40:", my_tuple.index(40))
print("Index of first occurrence of 30:", my_tuple.index(30))

# -------------------------------
# I. Positive and Negative Indexing
print("\nPositive Indexing: my_tuple[0] =", my_tuple[0])
print("Positive Indexing: my_tuple[3] =", my_tuple[3])
print("Negative Indexing: my_tuple[-1] =", my_tuple[-1])
print("Negative Indexing: my_tuple[-3] =", my_tuple[-3])

# II. Slicing Operations
print("\nSlicing: my_tuple[1:4] =", my_tuple[1:4])
print("Slicing with step: my_tuple[::2] =", my_tuple[::2])
print("Slicing from index 2 onwards: my_tuple[2:] =", my_tuple[2:])
print("Slicing till index 3: my_tuple[:3] =", my_tuple[:3])