# Lekcija #8 - Nastavak Lekcije #7
import time

products = {
    "hleb": {
        "cena": 100,
        "kolicina": 50
    },

    "pivo": {
        "cena": 150,
        "kolicina": 220
    },

    "maramice": {
        "cena": 60,
        "kolicina": 200
    },

}



# PRIKAZI NAJSKUPLJI PROIZVOD



answer = None
log_history = []
answer_list = ["a - Brisanje proizvoda", "b - Dodavanje proizvoda", "c - Lista proizvoda", "d - Istorijat", "e - Obrisi sve", "f - Prikazi najskuplji proizvod", "q - Izlazak"]

while answer != ["a", "b", "c", "d", "e"]:

    answer = input(f"Sta zelite da uradite? \n{answer_list}]\n : ").lower()
    if answer == "a":
        product = "nista"
        while product not in products:
            product = input("Unesite ime proizvoda za brisanje: ").lower()

        del products[product]
        msg = f"Proizvod {product} je izbrisan iz liste."
        print(msg)
        log_history.append(msg)
        print(products)
        print("\n")


    elif answer == "b":
        product = None

        while product in products or product is None:
            product = input("Unesite ime proizvoda koje zelite da dodate (ne postoji u listi): ")

        product_price = None
        while product_price is None or product_price <= 0:
            product_price = int(input("Unesite cenu proizvoda: "))

        product_amount = None
        while product_amount is None or product_amount < 0:
            product_amount = int(input("Unesite kolicinu proizvoda: "))

        products[product] = {
            "cena": product_price,
            "kolicina": product_amount
        }

        msg = f"Uneseni prozivod u listu je: {product}, cena: {product_price}, kolicina: {product_amount}"
        print(msg)
        log_history.append(msg)

    elif answer == "c":
        print(f"Trenutno stanje liste proizvoda je: {products}\n")

    elif answer == "d":
        print(log_history)
        print("\n")

    elif answer == "e":
        products.clear()
        msg = f"Vasa Lista je izbrisana!!!"
        log_history.append(msg)
        print(msg)

    elif answer == "f":
        max_price = 0
        for product in products:
            if products[product]["cena"]> max_price:
                max_price = products[product]["cena"]
                max_price_product = product
        msg = f"Najskuplji proizvod je {max_price_product}, {max_price})"
        print(msg)

    else:
        break

    answer = None

print(f"Finalna lista proizvoda je: {products}")

time.sleep(1)
print("Hvala sto ste koristili Banetovu skriptu, Ziveli!!!\nTHE END!!!")