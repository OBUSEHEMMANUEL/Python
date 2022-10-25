number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_number = list(filter(lambda x: x % 2 == 0, number))
print(new_number)
square_number = list(map(lambda x: x**2, number))
print(square_number)
new_square_number = list(map(lambda x: x**2,  filter(lambda x: x % 2 == 0, number)))
print(new_square_number)