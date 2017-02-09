import unittest
import sys
sys.path.append("../")
from Models.ShoppingCart import ShoppingCart

class TestShoppingCart():
    """
    A testsuit for the Shopping cart Feature of Bangazon CLI

    Methods:
    

    """

    def test_current_cart_should_be_ShoppingCart_object(self):
        """
        Method to test whether the ShoppingCart object id created correctly
        """
        current_cart = ShoppingCart()
        self.assertIsInstance(current_cart, ShoppingCart)
        

    def test_ShoppingCart_should_add_product(self):
        """
        Method to test whether the ShoppingCart object can add a product
        """
        product1 = (1, "Widget", "$5")
        product2 = (1, "FooBar", "$10")
        current_cart = ShoppingCart()
        self.assertEqual(current_cart.get_all_products(), [])
        current_cart.add_product(product1)
        self.assertEqual(current_cart.get_all_products(), [product1])
        current_cart.add_product(product2)
        self.assertEqual(current_cart.get_all_products(), [product1, product2])
