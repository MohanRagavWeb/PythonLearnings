def is_even(number):
  """Checks if a number is even."""
  return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(is_even, numbers)
even_numbers = list(filtered_numbers)

print(even_numbers)
# Output: [2, 4, 6, 8, 10]



nums = [1, 2, 3, 4, 5]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
