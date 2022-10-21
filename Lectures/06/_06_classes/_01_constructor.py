# class
class Person:
    info = "I'm a Person." # class instance
    # constructor
    def __init__(self, name, age):
        self.name = name # instance property
        self.age = age   # instance property

# instance
person_1 = Person('Alice', 20)
person_2 = Person('Bob', 25)


print('1:', person_1.name, person_1.age, person_1.info)
print('2:', person_2.name, person_2.age, person_2.info)

person_1.age += 1
print('3:', person_1.name, person_1.age)
print('4:', person_2.name, person_2.age)

person_1.info = "I'm not a person!"
print('5:', person_1.info)
print('6:', person_2.info)

Person.info = "I'm not a person!"
print('7:', person_1.info)
print('8:', person_2.info)

print('9:', person_1)
