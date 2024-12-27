# Napraviti listu proizvoda i ubaciti 3 proizvoda iPhone 14, iPhone 15, Samsung S23
# Napisati proveru koja proverava da li postoji "iPhone 14" u nasoj listi proizvoda


phone_list = ["iPhone 13", "iPhone 14", "Samsung S23"]
search_item = input("Unesite ime telefona koji trazite: ")
print(search_item)

if search_item in phone_list:
    print(f"Pronasli smo trazeni proizvod")
else:
    print("Nismo pronasli trazeni proizvod")