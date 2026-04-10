# PRACTICAL 7: Demonstrating Python Dictionary operations

# Creating a dictionary
student = {
    "name": "Vahib",
    "age": 21,
    "branch": "Computer Science"
}
print("Original Dictionary:", student)

# -------------------------------
# Updating dictionary
student["age"] = 22   # update age
student["branch"] = "Data Science"  # update branch
student["college"] = "ABC University"  # add new key-value pair
print("\nAfter updation:", student)

# -------------------------------
# Removing elements
student.pop("college")   # remove specific key
print("After removing 'college':", student)

# popitem() removes last inserted key-value pair
removed_item = student.popitem()
print("After popitem():", student, " | Removed:", removed_item)

# -------------------------------
# Dictionary methods

# clear()
temp_dict = student.copy()
temp_dict.clear()
print("\nAfter clear():", temp_dict)

# copy()
copied_dict = student.copy()
print("Copied Dictionary:", copied_dict)

# get()
print("Get 'name':", student.get("name"))

# items()
print("Items:", student.items())

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# len()
print("Length of dictionary:", len(student))

# sorted()
print("Sorted keys:", sorted(student))