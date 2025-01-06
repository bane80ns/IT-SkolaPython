# Product
# name, price, amount, type
from itertools import product


class Product:
    number_of_products = 0
    allowed_types = ["android", "ios"]
    amount_of_types = {
        "android": 0,
        "ios": 0
    }

    def __init__(self, name, price, amount, type):

        if amount < 1:
            raise ValueError("Amount must be more then zero")

        if type not in Product.allowed_types:
            raise ValueError("Invalid type")

        self.name = name
        self.price = price
        self.amount = amount
        self.type = type
        Product.number_of_products += 1

        Product.amount_of_types[type] += amount


# iPhone = Product("Iphone 14", 1000, 22, "phone")
#
# print(iPhone.name, iPhone.price, iPhone.amount, iPhone.type)
#
# samsung = Product("Samsung Galaxy", 1500, 20, "phone")
# print(samsung.name)