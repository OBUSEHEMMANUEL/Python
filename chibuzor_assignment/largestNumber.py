def maximum_value(list1):
    max_value = 0
    for list_array in list1:
        if list_array > max_value:
            max_value = list_array

    return max_value


listed = [2, 5, 7, 9, 3, 4, 1]
print(maximum_value(listed))


def maximum_number(arr):
    number = max(arr)


listed = [2, 5, 7, 9, 3, 4, 1]

print(maximum_value(listed))
