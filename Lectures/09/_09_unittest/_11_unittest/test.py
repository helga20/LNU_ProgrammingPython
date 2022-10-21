import unittest
from copy import deepcopy


class MyTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        from collection import Collection
        cls.persons = Collection()

    def setUp(self):
        self.persons_for_test = deepcopy(MyTest.persons)
        self.sorted_names = ['Ann', 'Ira', 'Roman']
        


    def test_sort(self):
        self.persons_for_test.sort()
        for person, name in zip(self.persons_for_test.persons, self.sorted_names):
            self.assertEqual(person.name, name)
        


if __name__ == "__main__":
    unittest.main()
