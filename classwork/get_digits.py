
def get_digit(number, position):
    """:return digit at position in number, counting from right"""

    return number//(10 ** position)%10

f = get_digit(4345,3)
print(f)


def get_lenght(number):
    return len(str(number))

def get_lenght2(number):
    return len(number)
#f = get_lenght(str(645768)
print(f)

def get_lenght3(number):
    import math
    return math.ceil(math.log10(number))

print(get_lenght3(456))

