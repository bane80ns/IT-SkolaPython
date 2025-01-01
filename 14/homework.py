#da li je email


import re

email_add = "bane@gmail.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email_add):
    print(email_add)