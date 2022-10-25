class Mydict(dict):
    def __setItem__(self, index, value):
        if not isinstance(index, str):
            raise TypeError("Can only take a string value")
        super().__setitem__(index, value)


Mydicy = Mydict()

Mydicy['1'] = 6
print(Mydicy)