class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old."

    # Python doesn't support overloading of methods
    # default values stay for it    
    def grown(self, years=1): 
        self.age += years

    def age_difference(self, other):
        return abs(self.age - other.age)


person_1 = Person('Alice', 20)
person_2 = Person('Bob', 30)

person_1.grown()
print('1:', person_1)

person_2.grown(5)
print('2:', person_2)

print('3:', person_1.age_difference(person_2))

