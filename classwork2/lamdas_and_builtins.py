# def add(a: int, b: int) -> int:
#     """Adds two numbers"""
#     return a + b
#

# print(add.__name__)
# print(add.__doc__)
# print(add.__annotations__)
import random


def operate(X, Y, func):
    return func(X, Y)


# print(operate(2, 3, add))
#
#
# def sub(X, Y):
#     return Y - X
#
#
# print(operate(5, 8, sub))


# def multiply(a):
#     def by(b):
#         return a * b
#
#     return by
#
#
# multiply_by_five = multiply(5)
# print(multiply_by_five(6))

adder = lambda a, b: a + b
print(adder(10, 9))
print(operate(2, 3, adder))
print(operate(2, 3, lambda a, b: a + b))
print(operate(2, 3, lambda a, b: b - a))
print(operate(2, 3, lambda w, y: w * y))

# import builtins
# whole number
# decimal places
print(round(56.78654, 2))
# significant figure
print(round(56.764672, -1))

# sum
arr = [1, 6, 4, 7, 2]
print(sum(arr, 100))

letters = [['a'], ['b', 'c'], ['d'], ['e', 'f']]
print(sum(letters, []))

fruits = "apple cucumber pear mango grape melon".split()
print(max(fruits))
print(max(fruits, key=lambda x: x[-3:]))

iterable1 = (1, 2, 3, 4)
iterable2 = ('hello', 'how', 'are', 'you')
print(dict(zip(iterable2, iterable1)))
print(list(zip(iterable2, iterable1, iterable2)))

s = 'hello'
print(sorted('hello', reverse=True))
print(sorted('chimamda adicha', reverse=True))

lst = [1, 2, 3, 4, 5]


def reduce_func(acc, item):
    print(f"acc --> {acc} <> item --> {item}")
    return acc + item


from math import prod

print("\n ############ Reduce ##########\n")

print(lst)
# print(reduce_func(reduce_func, lst, 100))
print(sum(lst, 100))
print(prod(lst))
print(prod(lst, start=100))
# print(lambda  acc, item: acc if acc > item else item, lst)
random.shuffle(lst)
print(lst)
print(max(lst))

print("\n ############ match ##########\n")

num = int(input("Enter a number"))
match num:
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print("Don't know you")

number = int(input("Enter a number"))
match number:
    case _ as x if 1 <= x <= 10:
        print(x)
    case _ as x if 11 <= x <= 20:
        print(x)

    case 30 | 40 | 50:
        print(x)
    case _:
        print("Don't know you")

lst = [20, 13, 16]

match lst:
    case [x, y, z]:
        print(x, y, z)

    case _:
        print("nothing matched")


def summing_list(list_: list[int]):
    match list_:
        case []:
            return 0
        case [first_value, *another_list]:
            return first_value + summing_list(another_list)
        case _:
            print("can only accept an int")
            return None


print(summing_list([1, 2, 3, 4, 5]))

import itertools

print(summing_list([1,2,3,4,5]))

print(list(itertools.zip_longest([1,2], [3,4,5], fillvalue = 0)))
