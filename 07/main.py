# Lekcija #7
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
while answer != "a" and answer != "b":
    print("Zeljeni izbor moze biti samo 'a' ili 'b'")
    answer = input("Sta zelite da uradite? \nBrisanje proizvoda = a\nDodavanje prozivoda = b\n").lower()

if answer == "a":
    product = "nista"
    while product not in products:
        product = input("Unesite ime proizvoda za brisanje: ").lower()
        print(product)

    del products[product]
    print(products)

elif answer == "b":

    product = None

    while product in products or product == None:
        product = input("Unesite ime proizvoda koje zelite da dodate (ne postoji u listi): ")

    productPrice = None
    while productPrice == None or productPrice <= 0:
        productPrice = int(input("Unesite cenu proizvoda: "))


    productAmount = None
    while productAmount == None or productAmount < 0:
        productAmount = int(input("Unesite kolicinu proizvoda: "))

    print(product, productPrice, productAmount)

    products[product] = {
        "cena": productPrice,
        "kolicina": productAmount
    }



    print("Ispisujemo TEST zato sto je dodavanje proizvoda u pripremi")

    # Dodati proizvod
    # Unesite ime proizvoda "mleko" -> products -> mleko
    # PS. Obavezno razmislite o svim mogucnostima
        # => Da li proizvod vec postoji (CAPS SENSITIVE)(Hleb, HLEB, hleb)
        # => Ime ne sme da bude manje od 2 char-a tipa "a"






print(products)
time.sleep(1)


print("THE NED")