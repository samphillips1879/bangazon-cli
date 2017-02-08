import sqlite3

class ProductData():
    def Product(self)
        with sqlite3.connect("Bangazon.db") as bang:
            cursor = bang.cursor()

            try:
                cursor.execute("SELECT * FROM Models.Product")
                products = cursor.fetchall()

            except sqlite3.OperationalError:
                