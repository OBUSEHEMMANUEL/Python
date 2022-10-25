list3 = [item ** 3 for item in range(1, 6)]
print(list3)

list2 = [item for item in range(1, 11) if item % 2 == 0]
print(list2)

list1 = [(x, x ** 3) for x in range(1, 6)]
print(list1)

list4 = [x for x in range(3, 30, 3)]
print(list4)

# TODO GENERATOR_EXPRESSION
for value in ( item ** 3 for item in range(1, 11) if item % 2 != 0):
    print(value, end='   ')
print(end="\n")

print(list (x ** 3 for x in [10, 3, 7, 1, 9, 4, 2]))


# def is_odd():
#     numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
#
#     print([item for item in numbers if item % 2 != 0 ])
#
# is_odd()

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0,  numbers) )))

list6 = [item ** 2 for item in numbers if item % 2 == 0]
print(list6)