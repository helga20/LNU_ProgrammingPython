class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str: # annotation for "must return string"
        return f"{self.name}, {self.age} years old."


person_1 = Person('Alice', 20)
person_2 = Person('Bob', 25)

print('1:', person_1)
print('2:', person_2)

# very important dictionary attribute
print('3:', person_1.__dict__)
print('4:', Person.__dict__)