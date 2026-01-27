def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]

squared_numbers_map = map(square, numbers)


print(list(squared_numbers_map))





salaries = [20000, 30000, 40000]

updated = list(map(lambda x: x + 5000, salaries))
print(updated)
