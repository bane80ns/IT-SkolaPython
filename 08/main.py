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

# print(products)
# Treba pitati korisnika (?) da unese ime proizvoda za brisanje
# Potencijalni problemi:
# 1. Korisnik ne unese nista
# 2. Sta ako korisnik unese ime prozivoda koji nemamo?
    # - While petlja dok ne unese tacan podatak
# 3. Uneo je ime prozivoda malim slovima

# product ne postoji u dict. products



answer = None
log_history = []
answer_list = ["a - Brisanje proizvoda", "b - Dodavanje proizvoda", "c - Lista proizvoda", "d - Istorijat", "e - Obrisi sve", "q - Izlazak"]

while answer != ["a", "b", "c", "d"]:
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
        current_event = ""

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
    else:
        break
    answer = None





    # Dodati proizvod
    # Unesite ime proizvoda "mleko" -> products -> mleko
    # PS. Obavezno razmislite o svim mogucnostima
        # => Da li proizvod vec postoji (CAPS SENSITIVE)(Hleb, HLEB, hleb)
        # => Ime ne sme da bude manje od 2 char-a tipa "a"

print(f"Finalna lista proizvoda je: {products}")
time.sleep(1)
print("Hvala sto ste koristili Banetovu skriptu, Ziveli!!!\nTHE END!!!")