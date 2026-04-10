# PRACTICAL 6: Demonstrating Python Set operations

# Creating a set
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)

# add()
set_a.add(10)
print("\nAfter add(10) in Set A:", set_a)

# clear()
temp_set = set_a.copy()
temp_set.clear()
print("After clear() on temp_set:", temp_set)

# copy()
copied_set = set_b.copy()
print("Copied Set B:", copied_set)

# difference()
print("\nDifference (A - B):", set_a.difference(set_b))

# intersection()
print("Intersection (A ∩ B):", set_a.intersection(set_b))

# union()
print("Union (A ∪ B):", set_a.union(set_b))

# isdisjoint()
print("\nIs A disjoint with B?:", set_a.isdisjoint(set_b))

# issubset()
print("Is {4,5} subset of A?:", {4, 5}.issubset(set_a))

# issuperset()
print("Is A superset of {1,2}?:", set_a.issuperset({1, 2}))