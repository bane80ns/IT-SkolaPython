import re

with open("logs/http.log", "r") as file:
    lines = file.readlines()

# Nadji rec Error praceno sa broja
error_pattern = r"Error \d{3}" # Pattern za "Error 333(3 cifre, ne mora biti 333)
status_pattern = r"Status \d{3}" # Pattern za "Status 333(3 cifre, ne mora biti 333)

# re.findall(pattern, lines)

with open("logs/errors.log", "a") as error_file, open("logs/success.log", "a") as status_file:
    for line in lines:
        if re.search(error_pattern, line):
                error_file.write(line)
        elif re.search(status_pattern, line):
                status_file.write(line)




