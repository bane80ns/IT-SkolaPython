# Pitati korisnika da unese ime proizvoda
# Kada unese ime proizvoda dodati proizvod u "kasu"
# Korisnik mora uneti 3 proizvoda ukupno


kasa = []
while len(kasa) < 3:
    proizvod = input("Unesite ime proizvoda: ")
    kasa.append(proizvod)
    print(f"\n Uspesno ste ubacili {proizvod} u kasu.")
print(f"Uspesno ste obavili kupovinu 3 proizvoda: {kasa}")
