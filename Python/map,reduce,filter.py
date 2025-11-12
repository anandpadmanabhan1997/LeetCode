numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]


numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]


from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24


