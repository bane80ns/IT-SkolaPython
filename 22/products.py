from db import Db

class Products(Db):

    number_of_products = 0
    allowed_types = ["android", "ios"]
    amount_of_types = {
        "android": 0,
        "ios": 0
    }


    def __init__(self):

        super().__init__()


    def create(self, name, price, amount, type):
        if amount < 1:
            raise ValueError("Amount must be more then zero")


        if type not in Products.allowed_types:
            raise ValueError("Invalid type")

        if self.check_if_product_exists(name) is not None:
            raise ValueError("Product with this name already exists")

        self.name = name
        self.price = price
        self.amount = amount
        self.type = type

        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO products (name, price, amount, type) VALUES (%s, %s, %s, %s)", (
                       name, price, amount, type
        ))
        self.connection.commit()
        cursor.close()


    def inc_ammount_of_products_for_type(self, type, amount):
        Products.number_of_products += 1
        Products.amount_of_types[type] += amount


    def check_if_product_exists(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name = %s", (name))
        self.connection.commit()

        result = cursor.fetchone()
        cursor.close()
        return result