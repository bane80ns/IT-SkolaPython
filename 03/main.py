# conditional statemens

name = "Tomaa"

# ako je ime "Toma" ispisi "Pozdrav Tomo"
# ako je ime neko drugo (ako nije Toma) ispisi "Pozdrav neko drugi"

if name == "Toma":
    print("Pozdrav Tomo")
else:
    print(f"Pozdrav {name}")


age = 44

# Uraditi proveru ako korisnik ima vise od 18g ispisati punoletni ste
# Ako korisnik ima manje od 18 godina ispisati "Niste punoletni"

if age >= 18:
    print("Punoletni ste")
else:
    print("Niste punoletni")

