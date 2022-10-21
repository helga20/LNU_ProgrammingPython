class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old."

    def grown(self, years=1): 
        self.age += years

    def age_difference(self, other):
        return abs(self.age - other.age)


class Employee(Person):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation

    def __str__(self):
        return f"{self.occupation.capitalize()} - {super().__str__()}"


employee_1 = Employee('Alice', 20, 'manager')

print('1:', employee_1.__class__)
print('2:', Employee.__name__)
print('3:', Employee.__bases__)
print('4:', Person.__bases__)