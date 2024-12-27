
cena_korpe = int(input("Unesite cenu korpe: "))
tax_amount = cena_korpe*0.10

if cena_korpe >= 1000:
    print(f"Ostvarili ste 10% popusta sto iznosi {tax_amount}")