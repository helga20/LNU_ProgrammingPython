from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    @abstractmethod
    def method(self):
        pass

class Sub(Super):
    pass

x = Sub()