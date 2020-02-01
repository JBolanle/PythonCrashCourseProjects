import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for get_city_country()"""

    def test_get_city_country(self):
        """Do inputs like 'Lagos, Nigeria' work?"""
        formatted_name = get_city_country('lagos', 'nigeria')
        self.assertEqual(formatted_name, 'Lagos, Nigeria')

    def test_city_country_population(self):
        """Tests if inputing a population will work"""
        formatted_Name = get_city_country('lagos', 'nigeria', 30000000)

unittest.main()