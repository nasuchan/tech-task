# coding=utf-8
import unittest
import tech_task

class TestGermanAddressParser(unittest.TestCase):
    """
    In these tests parching of different valid German addresses is checked.
    Parameter:
    - address in format Street + house number
    """
    germanAddressEasy = "Winterallee 3"
    germanAddressHarder = "Blau Feldweg 123B"
    germanAddressHardest = "Auf-der-Vogelwiese 23 b"
    germanAddressUmlauts = "Büselstraße 12"


    def test_parse_easy_german_address(self):
        parsed_address = tech_task.splitStreetGermanAddress(self.germanAddressEasy)
        self.assertEqual(parsed_address, '{"street": "Winterallee", "housenumber": "3"}')

    def test_parse_harder_german_address(self):
        parsed_address = tech_task.splitStreetGermanAddress(self.germanAddressHarder)
        self.assertEqual(parsed_address, '{"street": "Blau Feldweg", "housenumber": "123B"}')

    def test_parse_hardest_german_address(self):
        parsed_address = tech_task.splitStreetGermanAddress(self.germanAddressHardest)
        self.assertEqual(parsed_address, '{"street": "Auf-der-Vogelwiese", "housenumber": "23 b"}')

    def test_parse_german_address_umlauts(self):
        parsed_address = tech_task.splitStreetGermanAddress(self.germanAddressUmlauts)
        self.assertEqual(parsed_address, '{"street": "Büselstraße", "housenumber": "12"}')

class TestWorldAddressParser(unittest.TestCase):
    """
    In these tests parching of different valid addresses from 5 different countries is checked.
    Checked countries: USA, Spain, Argentina, France
    Parameter:
    - address in format Street + house number
    - country - one of supported countries
    """
    worldAddressUSA = "200 Broadway Av"
    worldAddressSpain = "Calle Aduana, 29"
    worldAddressFrance = "4, rue de la revolution"
    worldAddressArgentina = "Calle 39 No 1540"

    def test_parse_american_address(self):
        # Test for USA
        parsed_address = tech_task.splitStreetWorldAddress(self.worldAddressUSA, country="USA")
        self.assertEqual(parsed_address, '{"street": "Broadway Av", "housenumber": "200"}')

    def test_parse_spanish_address(self):
        # Test for Spain
        parsed_address = tech_task.splitStreetWorldAddress(self.worldAddressSpain, country="Spain")
        self.assertEqual(parsed_address, '{"street": "Calle Aduana", "housenumber": "29"}')

    def test_parse_french_address(self):
        # Test for France
        parsed_address = tech_task.splitStreetWorldAddress(self.worldAddressFrance, country="France")
        self.assertEqual(parsed_address, '{"street": "rue de la revolution", "housenumber": "4"}')

    def test_parse_angentine_address(self):
        # Test for Argentina
        parsed_address = tech_task.splitStreetWorldAddress(self.worldAddressArgentina, "Argentina")
        self.assertEqual(parsed_address, '{"street": "Calle 39", "housenumber": "No 1540"}')

class TestInvalidAddressesRaiseException(unittest.TestCase):
    """
    In these tests parching of different valid addresses from 5 different countries is checked.
    Checked countries: USA, Spain, Argentina, France
    Parameter:
    - address with a street name and a house number
    - country - one of supported countries
    """
    invalidAddressGerman = "Auf der Vogelwiese, 32"
    invalidAddressUSA = "Broadway Av 200"
    invalidAddressSpain = "Calle Aduana"
    invalidAddressFrance = "rue de la revolution 4"
    invalidAddressArgentina = "Calle 39 Number 1540"

    def test_parse_invalid_german_address(self):
        # Test for Germany - house nr. and street separated by a comma
        self.assertRaises(Exception, tech_task.splitStreetWorldAddress, self.invalidAddressGerman, country="Germany")

    def test_parse_invalid_american_address(self):
        # Test for USA - house nr. stays after street
        self.assertRaises(Exception, tech_task.splitStreetWorldAddress, self.invalidAddressUSA, country="USA")

    def test_parse_invalid_spanish_address(self):
        # Test for Spain - no house nr.
        self.assertRaises(Exception, tech_task.splitStreetWorldAddress, self.invalidAddressSpain, country="Spain")

    def test_parse_invalid_french_address(self):
        # Test for France - house nr. after street
        self.assertRaises(Exception, tech_task.splitStreetWorldAddress, self.invalidAddressFrance, country="France")

    def test_parse_invalid_angentine_address(self):
        # Test for Argentina - wrong identifier for house nr. "Number" instead of "No"
        self.assertRaises(Exception, tech_task.splitStreetWorldAddress, self.invalidAddressArgentina, country="Argentina")

    def test_parse_invalid_country_address(self):
        # Test for country - invalid country
        self.assertRaises(Exception, tech_task.splitStreetWorldAddress, self.invalidAddressArgentina, country="China")

if __name__ == '__main__':
    unittest.main()
