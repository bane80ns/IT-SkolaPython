import time

shops = {
    "Maxi": {
        "Hleb": 100,
        "Novine": 50
    },

    "Idea": {
        "Hleb": 110,
        "Novine": 40
    },

    "Roda": {
        "Hleb": 93,
        "Novine": 57
    },

    "Freeshop": {
        "Novine": 51
    }
}


for shop_name, items in shops.items():
    print(shop_name, items)

zbir = 0
br_prodavnica = 0

for shop_name, items in shops.items():
    # print(items["Hleb"])
    if "Hleb" not in items or items["Hleb"] == []:
        print(f"{shop_name} nema Hleb u ponudi.")
        continue
    else:
        zbir = items["Hleb"] + zbir
        br_prodavnica += 1
print(f"Prosecna cena hleba je: {zbir/br_prodavnica}")

time.sleep(1)


highest_price_bread = 0
max_bread_price_shop = ""

for shop_name, items in shops.items():
    # print(items["Hleb"])
    if "Hleb" not in items or items["Hleb"] == []:
        print(f"{shop_name} nema Hleb u ponudi.")
        continue
    else:
        if items["Hleb"] > highest_price_bread:
            highest_price_bread = items["Hleb"]
            max_bread_price_shop = shop_name

print(max_bread_price_shop, highest_price_bread)




