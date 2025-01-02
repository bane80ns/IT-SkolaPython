# BubbleSort

# Sortira elemente

# Uporedjuje
# Swap (menjanje)
# Mutliple pase - radi sve dok ne zavrsi te prve dve akcije

# numbers = [5, 1, 4, 2, 8]

# Pass 1:
# Uporedjuje 5 i 1 >>> 1, 5, 4, 2, 8
# Uporedjuje 5 i 4 >>> 1, 4, 5, 2, 8
# Uporedjuje 5 i 2 >>> 1, 4, 2, 5, 8

# Pass 2:
# Uporedjuje 1 i 4 >>> 1, 4, 2, 5, 8
# Uporedjuje 4 i 2 >>> 1, 2, 4, 5, 8
# Uporedjuje 4 i 5 >>> 1, 2, 4, 5, 8



numbers = [5, 1, 4, 2, 8]
numbers_length = len(numbers)


for i in range(numbers_length):

    swapped = False

    for j in range(0,numbers_length-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True

    if not swapped:
        break
print(numbers)