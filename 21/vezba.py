from products import Product
from shopingcart import ShoppingCart

iphone16 = Product("iPhone 16 pro max", 1500, 2, "ios")
samsungS23Pro = Product("Samsung S23 Pro", 1200, 200, "android")
samsungA55 = Product("Samsung A55", 500, 500, "android")
# hleb = Product("HLEB", 70, 1500, "food")

phoneCart = ShoppingCart()

phoneCart.addItem(iphone16)
phoneCart.addItem(iphone16)
# phoneCart.addItem(iphone16)

phoneCart.addItem(samsungS23Pro)
phoneCart.addItem(samsungS23Pro)
phoneCart.addItem(samsungS23Pro)
# phoneCart.addItem(samsungS23Pro)

# phoneCart.addItem(hleb)

# phoneCart.show_type_Total()



print(Product.amount_of_types["android"])


# phoneCart.addItem(samsungA55)



# phoneCart.showItems()

