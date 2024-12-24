# list

books = ["Harry Potter 1", "LOTR Collection", "Harry Potter 2"]

# Ispisite prvu stavku iz liste

print(books[0])

# Homework
# 1. Kako da promenite prvu stavku iz liste "Harry Potter 1" --> "Pragmatic Programmer"
# 2. Kako da obrisem poslednju stavku iz liste?

# Resenje:

# 1.
books[0] = "Pragmatic Programmer"
print(books)

# 2.
books.pop()
print(books)