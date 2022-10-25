def increment(number, by):
    return number + by


plcae_holder = increment(4, 5)
print(plcae_holder)


def func(*numbs):
    total = 0
    for numb in numbs:
        total += numb
    return total


def func1(**kwargs):
    print(kwargs)


func1(a=1, b=2, c=3, e=4)

lst = [3, 1, 7, 4, -3, 4]
print(func(*lst))

