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
employee_1.grown()

print('1:', employee_1)

