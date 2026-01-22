# Python Dictionary Methods Demonstration

print("=== DICTIONARY METHODS FULL DEMO ===")

# Create a dictionary
d = {
    "name": "Mohan",
    "age": 21,
    "course": "Data Engineering",
    "age": 21  # duplicate key overwritten
}
print("Original Dictionary:", d)

# 1. get() - Safe access to value
print("Get name:", d.get("name"))
print("Get city (default):", d.get("city", "Not Found"))

# 2. keys() - Get all keys
print("Keys:", d.keys())

# 3. values() - Get all values
print("Values:", d.values())

# 4. items() - Get all key-value pairs
print("Items:", d.items())

# 5. update() - Update or add key-value pairs
d.update({"city": "Chennai", "age": 22})
print("After update():", d)

# 6. setdefault() - Get or set default value
d.setdefault("salary", 50000)
print("After setdefault():", d)

# 7. pop() - Remove specific key
removed_age = d.pop("age")
print("After pop('age'):", d, "| Removed value:", removed_age)

# 8. popitem() - Remove last inserted key-value pair
last_item = d.popitem()
print("After popitem():", d, "| Removed:", last_item)

# 9. copy() - Copy dictionary
copy_dict = d.copy()
print("Copied Dictionary:", copy_dict)

# 10. clear() - Remove all elements
temp_dict = d.copy()
temp_dict.clear()
print("After clear():", temp_dict)

# 11. fromkeys() - Create dictionary from keys
keys = ["id", "name", "role"]
new_dict = dict.fromkeys(keys, "N/A")
print("fromkeys():", new_dict)

# 12. Membership test
print("Is 'name' in dictionary?", "name" in d)

# 13. len() - Length of dictionary
print("Dictionary length:", len(d))

# 14. Adding new key manually
d["experience"] = "Fresher"
print("After adding new key:", d)

# 15. Deleting key using del
del d["course"]
print("After del['course']:", d)

# 16. Loop through dictionary keys
print("\nLoop through keys:")
for key in d:
    print(key)

# 17. Loop through dictionary values
print("\nLoop through values:")
for value in d.values():
    print(value)

# 18. Loop through key-value pairs
print("\nLoop through items:")
for key, value in d.items():
    print(key, ":", value)

# 19. Dictionary Comprehension
squares = {x: x*x for x in range(5)}
print("\nDictionary Comprehension:", squares)

# 20. Nested Dictionary
employee = {
    "id": 101,
    "profile": {
        "name": "Mohan",
        "role": "DE Intern"
    }
}
print("\nNested Dictionary:", employee)
print("Access nested value:", employee["profile"]["name"])

# 21. Sorting Dictionary by Keys
sorted_keys = dict(sorted(d.items()))
print("\nSorted by keys:", sorted_keys)

# 22. Sorting Dictionary by Values
sorted_values = dict(sorted(d.items(), key=lambda x: x[1]))
print("Sorted by values:", sorted_values)

# 23. Convert list of tuples to dict
pair_list = [("a", 1), ("b", 2)]
converted = dict(pair_list)
print("\nConverted from list of tuples:", converted)

# 24. Merge dictionaries (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2
print("Merged dictionaries:", merged)

# 25. Frequency Counter Example (Real Use Case)
text = "banana"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("\nFrequency Count:", freq)

print("\n=== ALL DICTIONARY METHODS DEMONSTRATED SUCCESSFULLY ===")
