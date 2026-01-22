# Python Set Methods Demonstration

print("=== SET METHODS FULL DEMO ===")

# Create sets
s = {10, 20, 30, 40}
print("Original Set:", s)

# 1. add() - Add one element
s.add(50)
print("After add(50):", s)

# 2. update() - Add multiple elements
s.update([60, 70])
print("After update([60, 70]):", s)

# 3. remove() - Remove element (error if not found)
s.remove(20)
print("After remove(20):", s)

# 4. discard() - Remove element safely (no error)
s.discard(100)  # no error even if not found
print("After discard(100):", s)

# 5. pop() - Remove random element
removed = s.pop()
print("After pop():", s, "| Removed:", removed)

# 6. clear() - Remove all elements
temp_set = s.copy()
temp_set.clear()
print("After clear():", temp_set)

# 7. copy() - Copy set
copy_set = s.copy()
print("Copied Set:", copy_set)

# Create more sets for operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nSet A:", a)
print("Set B:", b)

# 8. union() - Combine sets
print("Union:", a.union(b))

# 9. intersection() - Common elements
print("Intersection:", a.intersection(b))

# 10. difference() - Elements in A not in B
print("Difference A-B:", a.difference(b))

# 11. symmetric_difference() - Elements in either but not both
print("Symmetric Difference:", a.symmetric_difference(b))

# 12. update() - Update set with union
temp = a.copy()
temp.update(b)
print("After update():", temp)

# 13. intersection_update() - Keep only common elements
temp = a.copy()
temp.intersection_update(b)
print("After intersection_update():", temp)

# 14. difference_update() - Remove elements found in another set
temp = a.copy()
temp.difference_update(b)
print("After difference_update():", temp)

# 15. symmetric_difference_update() - Keep unique elements only
temp = a.copy()
temp.symmetric_difference_update(b)
print("After symmetric_difference_update():", temp)

# 16. issubset() - Check subset
print("A is subset of B?", a.issubset(b))

# 17. issuperset() - Check superset
print("A is superset of B?", a.issuperset(b))

# 18. isdisjoint() - No common elements
print("A is disjoint with B?", a.isdisjoint(b))

# 19. Membership check
print("Is 3 in A?", 3 in a)

# 20. len() - Length of set
print("Length of A:", len(a))

# 21. max(), min(), sum()
print("Max of A:", max(a))
print("Min of A:", min(a))
print("Sum of A:", sum(a))

# 22. sorted() - Sorted list from set
print("Sorted Set A:", sorted(a))

# 23. Set comprehension
squares = {x*x for x in range(5)}
print("Set Comprehension:", squares)

# 24. Convert list to set (remove duplicates)
lst = [1, 2, 2, 3, 4, 4]
unique = set(lst)
print("Unique from list:", unique)

# 25. Frozenset (Immutable Set)
fs = frozenset([1, 2, 3])
print("Frozenset:", fs)

print("\n=== ALL SET METHODS DEMONSTRATED SUCCESSFULLY ===")
