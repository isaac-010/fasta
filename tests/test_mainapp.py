import unittest
from mainapp import get_price


class TestMainApp(unittest.TestCase):

    def test_price_list(self):
        price = get_price('soda')

        self.assertIsNotNone(price)
        self.assertEqual(price, " Price of the product named -> soda = 1")
