from methods import load_file, save_file


data = load_file("data/user.json")

data.append({
    "name": "Jelena Grozdic",
    "age": 22,
    "height": 170,
    "gender": "female"
})

save_file("data/user.json", data)

print(data)






