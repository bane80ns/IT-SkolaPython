# OOP

# Klase
# Osoba -> Ime, prezime, visina, tezina
# Product -> name, size, price, amount

# Klasa moze imati atribute (promenljive koje su vezane za klasu), metode / def / funkcije
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def write_my_name(self):
        print(self.name, self.age) # Ispisi ime i godine od ovog objekta



# Objekti
# class Product -> "hleb", 123, 90, 1
# class Product -> "krompir", 12, 123, 12

bane = Person("Branislav", "44") # Napravili smo novi objekat
# bane.write_my_name()

marko = Person("Marko", 18)
marko.write_my_name()






