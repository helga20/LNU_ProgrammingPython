class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old."

    def __add__(self, other): 
        return self.age + other.age

    """ def __radd__(self, other):
        return self.age + other """


person_1 = Person('Alice', 20)
person_2 = Person('Bob', 25)
person_3 = Person('Mary', 15)

print('1:', person_1 + person_2)

persons = [person_1, person_2, person_3]

print('2:', sum(persons))