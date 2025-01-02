# Algoritmi
# Sort, BubbleSort, Factorial Calculation

# Linear Search
# Nadji najveci broj u listi

nums = [3, 5, 2, 12, 8, 1]

# Neka max broj po def bude prvi broj
max_num = nums[0]

# predji preko svih brojeva iz liste
# ako je trenutni max broj manji, onda je taj iz petlje max

for num in nums:
    if num > max_num:
        max_num = num

print(max_num)

# Vezba: Pronaci broj 8

searchable_num = 8
for num in nums:
    if num == searchable_num:
        print("Pronasli smo zeljeni broj.")
        break

# Nadji koliko puta se ponavlja 8
# Nadji koliko puta se nesto ponavlja iz liste
# Proveri duplikate



