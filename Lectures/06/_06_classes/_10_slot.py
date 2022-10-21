class Person:
    __slots__ = ['name', 'age', 'gender']

    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('Alice', 20)
person.age = 22
person.gender = 'male'
person.weight = 75