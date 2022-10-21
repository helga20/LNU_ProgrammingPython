def to_upper_case(self):
    return self.name.upper()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old."


person = Person('Alice', 20)

print('1:', to_upper_case(person))

Person.name_to_upper_case = to_upper_case

print('2:', person.name_to_upper_case())

def name_upper_case(self):
    self.name = self.name.upper()

Person.name_to_upper_case = name_upper_case
person.name_to_upper_case()
print(person)
