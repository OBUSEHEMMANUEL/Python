def add(a: float, b: float) -> float | None:
    try:
        # lst = [1,2,3]
        # print(lst[6])
        # name = int('great')
        # file = open('file.txt', mode='r', encoding='utf - 8')
        # print(file.read())
        # print("About to close")
        # file.close()
        print(a / b)
    except ZeroDivisionError:
        print("can't divide with zero")
        return None
    except (TypeError, NameError, ValueError):
        print("TYPE Error")
    except IndexError:
        print("index out of bound")
    except FileNotFoundError:
        print("file not found")
    else:
        print("owo epo")
    finally:
        print("About to close")


print(add(1, 2))
