import unittest
from city_functions import get_city_info


class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_get_city_info(self):
        """Test that function accepts City, Country"""
        formated_city = get_city_info('ireland', 'dublin')
        self.assertEqual(formated_city, 'Ireland, Dublin')

    def test_city_country_population(self):
        """Test that function accepts City, Country, Population"""
        formated_city = get_city_info('ireland', 'dublin', '10_000_000')
        self.assertEqual(formated_city, 'Ireland, Dublin, 10_000_000')


if __name__=='__main__':
    unittest.main()