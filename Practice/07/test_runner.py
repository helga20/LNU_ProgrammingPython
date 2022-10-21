from functions import *
import unittest


class FuncsTest(unittest.TestCase):

        def test_count_even(self):
                self.assertEqual(count_even([3, 6, 5, 4, 2]), 3)
                self.assertEqual(count_even([5, 3]), 0)
                self.assertEqual(count_even([0, -2, -4, -6, -3]), 4)
                self.assertEqual(count_even([0, 2, -4]), 3)
                self.assertNotEqual(count_even([0, 2, -4]), 2)

        def test_days_in_yearn(self):
                self.assertEqual(days_in_year(2020), 366)
                self.assertEqual(days_in_year(2022), 365)
                self.assertEqual(days_in_year(-2), 0)
                self.assertEqual(days_in_year(0), 0)
                self.assertNotEqual(days_in_year(2022), 366)
                self.assertRaises(TypeError, days_in_year, -2, 365)


if __name__ == '__main__':
    unittest.main()


