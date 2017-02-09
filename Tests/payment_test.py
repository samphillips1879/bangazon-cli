import unittest
import sys
sys.path.append("../")
from models.payment import *

class TestPayment(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # self.payment = Payment()
        self.juan_payment_current_account = Payment(1, "Visa", "12345678")
        self.taylor_payment_current_account = Payment(2, "Mastercard", "87654321")
        self.juan_payment_all_accounts =
        self.taylor_payment_current_accounts =


    def test_user_payment_is_a_user_payment(self):
        self.assertIsInstance(self.juan_payment, Payment)

        self.assertIsInstance(self.taylor_payment, Payment)

    def test_user_can_enter_payment_credentials(self):
        self.assertEqual(self.juan_payment.get_payment_type(), "Visa")
        self.assertEqual(self.juan_payment.get_account_number(), "12345678")

    def test_can_get_full_payment_info_current_account_and_current_user(self):
        self.assertIn((1, "Visa", "12345678"), self.juan_payment.get_full_payment_info_current_account_current_user())

    def test_can_get_all_accounts_for_current_user(self):
        self.



    # def test_payment_is_posted(self):
    #     payment = payment_is_posted(self.juan_payment)
    #     self.assertTrue()


    # def test_user_payment_is_returning_as_a_tuple(self):
    #     payment = self.juan_payment.get_full_payment_info()
    #     self.assertTrue(payment, get_full_payment_info(self.juan_payment))

if __name__ == "__main__":
    unittest.main()



