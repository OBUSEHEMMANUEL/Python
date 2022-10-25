def maximum_value(list1):
    max_value = 0
    for list_array in list1:
        if list_array > max_value:
            max_value = list_array

    return max_value


listed = [2, 5, 7, 9, 3, 4, 1]
print(maximum_value(listed))


def maximum_number():
    list2 = [2, 5, 7, 9, 3, 4, 1]
    list.reverse(list2)
    print(list2)


maximum_number()


def calculate_product(*args):
    product = 1
    for i in args:
        product *= i
    return product


print(calculate_product(10, 20, 30))
print(calculate_product(1,6,2))
