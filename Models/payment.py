# import sqlite3

class Payment():

    def __init__(self, customer_id, payment_type, account_number):
        self.__customer_id = customer_id
        self.__payment_type = payment_type
        self.__account_number = account_number
        self.__full_payment_info_current_account_current_user = [(1 ,"Visa", "12345678"), (2, "MC", "34534")]
        self.__all_payment_info_current_user = []

    def get_payment_type(self):
        return self.__payment_type

    def get_account_number(self):
        return self.__account_number

    def get_full_payment_info_current_account_current_user(self):
        # self.__full_payment_info.append(self.__payment_type)
        # self.__full_payment_info.append(self.__account_number)
        return self.__full_payment_info_current_account_current_user

    # def get_all_payment_info_for_current_user(self):

    def payment_info_is_posted(self):
        pass

    def payment_info_can_be_returned(self):
        pass





