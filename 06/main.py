# Array (list) 5 students:
# Every student: name: , score: 0-100, active: true/false

student_list = [
    {
        "name": "Toma",
        "score": 89,
        "active": True
    },

    {
        "name": "Branislav",
        "score": 77,
        "active": True
    },

    {
        "name": "Dejan",
        "score": 99,
        "active": True
    },

    {
        "name": "Petar",
        "score": 12,
        "active": False
    },

    {
        "name": "Marija",
        "score": 47,
        "active": False
    }
]

for student in student_list:

    if not student["active"]:
        continue

    if student["score"] >= 80:
        student["grade"] = "A"
    elif 80 > student["score"] >= 60:
        student["grade"] = "B"
    elif 60 > student["score"] >= 40:
        student["grade"] = "C"
    elif 40 > student["score"] >= 20:
        student["grade"] = "D"
    else:
        student["grade"] = "F"
print(student_list)

# Ako je score studenta (ovo vazi SAMO za aktivne studente)
#