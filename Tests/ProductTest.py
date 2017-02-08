import unittest
import sys
sys.path.append("../")
from Models.Product import Product



class TestProduct(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.shampoo  = Product("Coconut Oil Shampoo", "7.99", "silky smoothe hair treatment shampoo")

    def test_product_has_all_the_attributes(self):
        self.assertIsNotNone(self.shampoo.price)
        self.assertIsNotNone(self.shampoo.name)
        self.assertIsNotNone(self.shampoo.description)

if __name__ =='__main__':
     unittest.main()