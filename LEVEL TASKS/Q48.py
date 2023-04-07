def even(num):
    return num % 2 == 0


even_numbers = list(filter(even, range(1, 21)))


print(even_numbers)
