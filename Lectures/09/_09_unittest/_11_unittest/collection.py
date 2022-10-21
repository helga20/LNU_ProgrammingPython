from person import Person


class Collection:
    def __init__(self, filename='data.txt'):
        self.persons = []
        self.filename = filename
        self.create()

    def create(self):
        with open(self.filename, encoding='utf-8') as f:
            for line in f:
                parts = line.split(', ')
                name = parts[0].strip()
                age = parts[1].strip()
                self.persons.append(Person(name, age))

    def sort(self):
        self.persons.sort(key=lambda x: x.name)

    def __str__(self):
        return '\n'.join(map(str, self.persons))
