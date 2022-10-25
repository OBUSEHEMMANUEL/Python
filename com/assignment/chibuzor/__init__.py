x = 7


def access_global():
    print(x)


access_global()


def modify():
    global x
    x = 3.5
    print(x)


modify()


def check():
    print("check", x)


check()


def cube(x):
    return x ** 3


print("The cube of 2 is", cube(2))
