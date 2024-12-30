

def hello_world():
    print("Hello World")


city = input("Unesite ime grada za koji zelite da se obavi dostava: ")


def calculate_delivery(city):
    if city == "Beograd" or city == "Zagreb":
        print("Dostava je 500 din.")
    elif city == "Subotica":
        print("Dostava je 1200 din.")
    elif city == "Novi Sad":
        print("Dostava je 700 din.")
    elif city == "Split":
        print("Dostava je 1300 din.")
    else:
        print("Grad ne postoji!")


calculate_delivery(city)

def calculate(number1, number2):
    return(number1+number2)

result = calculate(22,64)*2
print(result)

calculate(5,27)