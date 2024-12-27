# Pitati korisnika za godine
# Ako ima 18 ili vise godina >> "Punoletni Ste"
# Ako ima manje od 18 >> "Maloletni ste"

age = input("Unesite koliko imate godina: ")
age_integer = int(age)
if age_integer >= 18:
    print("Punoletni Ste!")
else:
    print("Maloletni ste.")