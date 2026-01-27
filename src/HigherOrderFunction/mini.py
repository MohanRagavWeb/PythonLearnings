from functools import reduce

nums = [5, 10, 15, 20]

double = list(map(lambda x: x * 2, nums))
print("Doubled:", double)

filtered = list(filter(lambda x: x > 20, double))
print("Filtered:", filtered)

summed = reduce(lambda a, b: a + b, filtered)
print("Sum:", summed)
