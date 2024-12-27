
products = {"iphone 14": 999, "iphone 15": 1200, "samsung s23": 1200}

search_product = input("Unesite ime proizvoda: ").lower()

if search_product in products:
    print(products[search_product])
else:
    print("Proizvod nije pronadjen")