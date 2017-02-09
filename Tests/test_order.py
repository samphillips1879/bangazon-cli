import unittest
import sys
sys.path.append("../")
from Models.Order import Order

class TestOrder():
    """
    A testsuit for the Order Feature of Bangazon CLI

    Methods:
    test_current_order_should_be_ShoppingCart_object
    test_Order_should_close_current_order
    """