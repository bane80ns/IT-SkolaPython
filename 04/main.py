

korisnik = int(input("Unesite vase godine: "))


if korisnik < 0:
    print("Godine ne mogu biti manje od 0")
    quit()

if korisnik <= 12:
    print("Vi ste dete.")
elif 12 < korisnik < 18:
    print("Vi ste tinejdzer.")
elif 18 <= korisnik < 65:
    print("Vi ste odrasla osoba.")
else:
    print("Vi ste penzionier.")