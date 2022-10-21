class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old."

    def __lt__(self, other): # <
        return self.age < other.age


class Employee(Person):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation

    def __str__(self):
        return f"{self.occupation.capitalize()} - {super().__str__()}"


class Staff:
    def __init__(self, staff=[]):
        self.staff = staff

    def __add__(self, employee):
        self.staff.append(employee)

    def __str__(self):
        s = 'Staff:\n'
        for employee in self.staff:
            s += str(employee) + '\n'
        return s

    def sort(self):
        self.staff.sort()

employee_1 = Employee('Alice', 20, 'manager')
employee_2 = Employee('Bob', 25, 'operator')
employee_3 = Employee('Mary', 15, 'manager')

staff = Staff()
for item in [employee_1, employee_2, employee_3]:
    staff + item
print(staff)

staff.sort()
print(staff)