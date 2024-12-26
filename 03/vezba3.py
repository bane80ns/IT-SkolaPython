name = "admin"
password = "mojaSifra"

# Ako ime admin i AKO je sifra mojaSifra
# Ako je ime "toma" i ako je sifra "123456"
# Ako je ime "marija" i ako je sifra "554231" print dobdrodosla Marija

if name == "admin" and password == "mojaSifraa":
    print("Dobrodosao admine!")
elif name == "toma" and password == "123456":
    print("Dobrodosao Tomo")
elif name == "marija" and password == "554231":
    print("Dobrodosla Marija")
else:
    print("Niste administrator! pogresna sifra ili ime")