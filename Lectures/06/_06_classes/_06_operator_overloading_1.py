class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old."

    def __add__(self, x):
        self.age += x


person_1 = Person('Alice', 20)
person_1 + 3
print('1:', person_1)