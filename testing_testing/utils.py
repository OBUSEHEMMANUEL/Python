import doctest

#
# def add(x, y):
#     assert x > 0 and y > 0, "Numbers cannot be negative"
#     assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "only int and float can be added "
#     return x + y
#
#
# print(add(2, 3))
#
#
# def mylst(lst1, lst2):
#     assert isinstance(lst1, list) and isinstance(lst2, list), "list must be passed"
#     return lst1 + lst2
#
#
# num = [1, 2, 3]
# num2 = [4, 5, 6]
# print(mylst(num, num2))
from testing_testing.exception import MycustomException


def add(x, y):
    """ adds two numbers
    >>> add(5,5)
    10
    >>> add(2,-6)

     >>>  add(2,"hi") # doctest: +IGNORE_EXCEPTION_DETAIL

     Traceback (most recent call last)
     ...
     TypeError:

    """
    if x > y:
        raise MycustomException("just fooling around")
    return x + y


if __name__ == "__main__":
    doctest.testmod()
