class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old."

    def __lt__(self, other): # <
        return self.age < other.age


person_1 = Person('Alice', 20)
person_2 = Person('Bob', 25)
person_3 = Person('Mary', 15)

print('1:', person_1 < person_2)

print('2:', person_2 < person_3)

persons = [person_1, person_2, person_3]
persons.sort()
print('3:', *map(str, persons))