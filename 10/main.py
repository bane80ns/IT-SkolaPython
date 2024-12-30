import json

# json file loading "r" - read
with open("data.json", "r") as file:
    data = json.load(file)
    data.append({
        "name": "Petar Petrovic",
        "age": 35,
        "height": 190,
        "gender": "male"
    })

print(data)

# jason file write "w"
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)