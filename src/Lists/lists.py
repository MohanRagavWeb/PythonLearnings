# Python List Methods Demonstration

print("=== LIST METHODS FULL DEMO ===")

# Create a list
lst = [10, 20, 30, 40, 20]
print("Original List:", lst)

# 1. append() - Add one element at the end
lst.append(50)
print("After append(50):", lst)

# 2. extend() - Add multiple elements
lst.extend([60, 70])
print("After extend([60, 70]):", lst)

# 3. insert() - Insert element at specific index
lst.insert(2, 99)
print("After insert(2, 99):", lst)

# 4. remove() - Remove first occurrence of value
lst.remove(20)
print("After remove(20):", lst)

# 5. pop() - Remove element by index (default: last)
lst.pop()
print("After pop():", lst)

lst.pop(0)
print("After pop(0):", lst)

# 6. clear() - Remove all elements
temp_list = lst.copy()
temp_list.clear()
print("After clear():", temp_list)

# 7. index() - Find index of element
index_val = lst.index(30)
print("Index of 30:", index_val)

# 8. count() - Count occurrences of element
count_val = lst.count(20)
print("Count of 20:", count_val)

# 9. sort() - Sort list ascending
lst.sort()
print("After sort():", lst)

# 10. sort(reverse=True) - Sort descending
lst.sort(reverse=True)
print("After sort(reverse=True):", lst)

# 11. reverse() - Reverse list order
lst.reverse()
print("After reverse():", lst)

# 12. copy() - Copy list
copied_list = lst.copy()
print("Copied List:", copied_list)

# 13. del - Delete elements by index or range
del lst[0]
print("After del lst[0]:", lst)

# 14. list() - Convert iterable to list
new_list = list((1, 2, 3))
print("Using list() constructor:", new_list)

# 15. len() - Get list length
print("Length of list:", len(lst))

# 16. max() - Get maximum value
print("Max value:", max(lst))

# 17. min() - Get minimum value
print("Min value:", min(lst))

# 18. sum() - Sum of values
print("Sum of list:", sum(lst))

# 19. sorted() - Return sorted list without modifying original
sorted_list = sorted(lst)
print("Sorted List (new):", sorted_list)

# 20. Membership check
print("Is 30 in list?", 30 in lst)

# 21. Concatenation (+)
combined = lst + [100, 200]
print("After concatenation:", combined)

# 22. Repetition (*)
repeated = lst * 2
print("After repetition:", repeated)

# 23. Loop through list
print("Looping through list:")
for item in lst:
    print(item)

# 24. List slicing
print("Slicing lst[1:4]:", lst[1:4])
print("Reverse slicing lst[::-1]:", lst[::-1])

# 25. List comprehension
squares = [x*x for x in range(5)]
print("List comprehension (squares):", squares)

print("\n=== ALL LIST METHODS DEMONSTRATED SUCCESSFULLY ===")
