from functools import reduce

data = [3, 2, 5, 4, 1]
max_element = reduce(lambda x, y: x if x > y else y, data)
# Result: 5
print(f"The maximum element is: {max_element}")



from functools import reduce

nums = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, nums)
print(total)
