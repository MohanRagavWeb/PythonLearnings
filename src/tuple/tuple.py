# Python Tuple Methods Demonstration

print("=== TUPLE METHODS FULL DEMO ===")

# Create tuples
t = (10, 20, 30, 20, 40)
print("Original Tuple:", t)

# 1. count() - Count occurrences of a value
count_20 = t.count(20)
print("Count of 20:", count_20)

# 2. index() - Find index of a value
index_30 = t.index(30)
print("Index of 30:", index_30)

# Accessing tuple elements
print("\nAccessing Elements:")
print("First element:", t[0])
print("Last element:", t[-1])

# Tuple slicing
print("\nTuple Slicing:")
print("t[1:4]:", t[1:4])
print("t[::-1] (Reversed):", t[::-1])

# Tuple immutability demonstration
print("\nTuple Immutability Demo:")
try:
    t[0] = 100
except TypeError:
    print("Error: Tuples are immutable (cannot modify elements)")

# Convert tuple to list to modify
print("\nModifying Tuple via List Conversion:")
temp_list = list(t)
temp_list.append(50)
t_modified = tuple(temp_list)
print("Modified Tuple:", t_modified)

# Tuple concatenation
print("\nTuple Concatenation:")
t2 = (50, 60)
combined = t + t2
print("Combined Tuple:", combined)

# Tuple repetition
print("\nTuple Repetition:")
repeated = t * 2
print("Repeated Tuple:", repeated)

# Membership test
print("\nMembership Test:")
print("Is 30 in tuple?", 30 in t)

# Tuple length
print("\nTuple Length:")
print("Length of tuple:", len(t))

# max(), min(), sum()
print("\nTuple Numeric Functions:")
print("Max value:", max(t))
print("Min value:", min(t))
print("Sum of values:", sum(t))

# sorted() - Returns sorted list from tuple
print("\nSorted Tuple:")
print("Sorted:", sorted(t))

# Loop through tuple
print("\nLoop Through Tuple:")
for item in t:
    print(item)

# Tuple packing
print("\nTuple Packing:")
packed = 1, 2, 3
print("Packed Tuple:", packed)

# Tuple unpacking
print("\nTuple Unpacking:")
a, b, c = packed
print("a =", a, "| b =", b, "| c =", c)

# Swapping values using tuple
print("\nSwapping Values:")
x, y = 10, 20
x, y = y, x
print("x =", x, "| y =", y)

# Nested tuple
print("\nNested Tuple:")
nested = ((1, 2), (3, 4))
print("Nested Tuple:", nested)
print("Access nested element:", nested[0][1])

# Returning multiple values from a function
print("\nTuple Return from Function:")

def get_values():
    return (100, 200, 300)

val1, val2, val3 = get_values()
print("Returned values:", val1, val2, val3)

# Single-element tuple
print("\nSingle Element Tuple:")
single = (99,)
print("Single Tuple:", single)

# Convert list to tuple
print("\nConvert List to Tuple:")
lst = [1, 2, 3]
converted = tuple(lst)
print("Converted Tuple:", converted)

print("\n=== ALL TUPLE METHODS DEMONSTRATED SUCCESSFULLY ===")
