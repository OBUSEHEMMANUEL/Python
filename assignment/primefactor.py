def prime_number(number):
    square_number = number * number
    number_str = str(number)
    square_number_str = str(square_number)
    length_number = len(number_str)
    check_count = square_number_str[-length_number:]

    if number_str == check_count:
        return print(f'{number} is anagram of {square_number}')
    else:
        return print(f'{number} is not an anagram of {square_number}')


prime_number(int(input("ENTER NUMBER: ")))
