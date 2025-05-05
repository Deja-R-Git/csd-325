#Juedeja Richard - Module7.2 -4/27/25
#this program tests city_functions.py to make sure it results in the correct string

import unittest
from city_functions import format_city_country
Yes = format_city_country("city_name", "country_name",
                          "language_type", "population_num")

class TestCities(unittest.TestCase):
    def test_format_city_country(self):
        self.assertEqual('yes'.capitalize(), "Yes")

    def test_capitalize(self):
        self.assertTrue('Yes'.istitle())
        self.assertFalse('yes'.istitle())

    def test_split(self):
        s = 'Houston Texas English 123456'
        self.assertEqual(s.split(), ['Houston','Texas','English','123456'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__=='__main__':
    unittest.main()