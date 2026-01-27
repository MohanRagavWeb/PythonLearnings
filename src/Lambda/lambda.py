nums = [5, 2, 9, 1]

# Sort using lambda
sorted_nums = sorted(nums, key=lambda x: x)
print("Sorted:", sorted_nums)

# Square using lambda
square = lambda x: x * x
print("Square of 4:", square(4))

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)
