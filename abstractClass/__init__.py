import abc


# class Mammal(metaclass=abc.ABCMeta):

class Mammal(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass


class Person(Mammal):
    def move(self):
        pass


p1 = Person()
