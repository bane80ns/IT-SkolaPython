# Fibbonaci
# Saberi poslednja 2 broja

#Sabiraj do 100
# [0,1]
# 0+1 = 1, [0, 1, 1]
# 1+1 = 2, [0, 1, 1, 2]
# 1+2 = 3, [0, 1, 1, 2, 3]
# 2+3 = 5, [0, 1, 1, 2, 3, 5]
# 3+5 = 8, [0, 1, 1, 2, 3, 5, 8]
# 5+8 = 13 [0, 1, 1, 2, 3, 5, 8, 13]

# OVAKO SAM JA RAZUMEO ZADATAK, tj dosao do resenja
"""
x = 0
y = 1
b = [0,1]
for i in range(100):
    z = x + y
    x = y
    y = z
    if z > 100:
        break
    b.append(z)
print(b)
"""


numbers = [0, 1]

while numbers[-1] < 100:

    next_number = numbers[-1] + numbers[-2]

    if next_number > 100:
        break
    numbers.append(next_number)
print(numbers)

