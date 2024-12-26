# Napraviti novi fajl "vezba.py", napraviti novu listu koja sadrzi 3 marke automobila.

cars = ["Audi", "BMW", "Zastava" ]

print(cars)

# BMW -> Mercedes

cars[1] = "Mercedes"
print(cars)

#Dodati jos 1 automobil na kraj "Skoda"

cars.append("Skoda")
print(cars)

# Sortirajte cars A-Z

cars.sort()
print(cars)

# Trenutno na stanju imamo x automobila

print(F"Trenutno na stanju imamo {len(cars)} automobila.")