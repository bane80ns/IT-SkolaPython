import re

ourNumber = "12345" #Da li se ovde nalaze samo brojevi


# r - (malo slovo r) prdstavlja da mi trazimo i tretiramo ceo string kao obican tekst
    # \ escape char

# ^ - trazimo od pocetka string-a
# \d - match (trazi samo brojeve) - trazi poklapanje - poklapanje
# + da ne pronadje samo prvi char, nego nastavalja do kraja
# $ kraj string-a

pattern = r"^\d+$"


# proveri da li su samo brojevi unutar necega:

if re.match(pattern, ourNumber):
    print("samo brojevi")
else:
    print("nisu samo brojevi")


sentence = "I love python"

# Character class: [a-z]
letterpattern = r"^[a-zA-Z ]+$"

if re.match(letterpattern,sentence):
    print("Only letters")
else:
    print("Not only letters")

# da li recenica pocinje velikim slovom
importantSentence = "Today will rain"
capital_letter_pattern = r"[A-Z]"

if re.match(capital_letter_pattern, importantSentence):
    print("Recenica pocinje velikim slovom")
else:
    print("Recenica NE pocinje velikim slovom")

phone_num = "385234234"
phone_pattern = r"^381"

if re.match(phone_pattern, phone_num):
    print("Pocinje sa 381")

# 381, 382, 385, 389
# serbia, ,montenegro, Bosnia and Hercegovina, Croatia

phone_pattern_balkan = r"^38(1|2|5|9)"

phone_match = re.match(phone_pattern_balkan,phone_num)
print(phone_match)
print("\n")

phone_map = {
    381: "Serbia",
    382: "Montenegro",
    385: "Bosnia and Herzegovina",
    389: "Croatia"
}


if phone_match:
    prefix = "38"+phone_match.group(1)
    print(f"Prefix number is {prefix} and matching country is {phone_map[int(prefix)]}")



