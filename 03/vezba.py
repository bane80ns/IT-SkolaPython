age = 44
allowed_age = 18

# Uraditi proveru ako korisnik ima vise od 18g ispisati punoletni ste
# Ako korisnik ima manje od 18 godina ispisati "Niste punoletni"

if age >= allowed_age:
    print("Punoletni ste")
else:
    print("Niste punoletni")


print(f"Korisnik ima vise od {age-allowed_age} razlike")