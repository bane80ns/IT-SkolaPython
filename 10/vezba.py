# from methods.py load def load_file
from methods import load_file, save_file

products = load_file("data/products.json")
user = load_file("data/user.json")

print(products, user)