from products import Products
from shopingcart import ShoppingCart

iphone16 = Products()
samsungS23Pro = Products()
samsungA55 = Products()


iphone16.create("iPhone 16 pro max", 1500, 2, "ios")
iphone16.inc_ammount_of_products_for_type("ios", 2)

samsungS23Pro.create("Samsung S23 Pro", 1200, 200, "android")
samsungS23Pro.inc_ammount_of_products_for_type("android", 200)

samsungA55.create("Samsung A55", 500, 500, "android")
samsungA55.inc_ammount_of_products_for_type("android", 500)




phoneCart = ShoppingCart()

phoneCart.addItem(iphone16)
phoneCart.addItem(iphone16)
# phoneCart.addItem(iphone16)

phoneCart.addItem(samsungS23Pro)
phoneCart.addItem(samsungS23Pro)
phoneCart.addItem(samsungS23Pro)
# phoneCart.addItem(samsungS23Pro)
