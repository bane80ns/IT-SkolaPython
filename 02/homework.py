# Napraviti dict koji ima sledecu strukturu
# person1 "name": "Toma", "last_name": "Nikolic"
# person2 "name": "Petar", "last_name": "Pavlovic"
# person3 "name": "Mihajlo", "last_name": "Folic"


people = {
    "person1": {
        "name": "Toma",
        "last_name": "Nikolic"
    },
    "person2": {
        "name": "Petar",
        "last_name": "Pavlovic"
    },
    "person3": {
        "name": "Mihajlo",
        "lastname": "Folic"
    }
}

print(people["person3"]["name"], people["person1"]["last_name"])
