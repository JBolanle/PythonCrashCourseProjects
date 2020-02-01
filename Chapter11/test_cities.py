import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for get_city_country()"""

    def test_get_city_country(self):
        """Do inputs like 'Lagos, Nigeria' work?"""
        formatted_name = get_city_country('lagos', 'nigeria')
        self.assertEqual(formatted_name, 'Lagos, Nigeria')

unittest.main()