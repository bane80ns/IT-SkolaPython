
# virt. biblioteka
# CRUD
# Dodaj knjigu
# Izlistaj knjigu
# Obrisi knjigu

books = []

def add_book(book_name, book_author):
    books.append({"name": book_name, "author": book_author})


def find_book_by_name(book_name):
    for book in books:
        if book["name"] == book_name:
            return book


def delete_book_by_name(book_name):

    search_books = find_book_by_name(book_name)
    if search_books is None:
        print("Knjiga koju trazite ne postoji")
    else:
        books.remove(search_books)


add_book("The Fog", "Steven King")
add_book("Na Drini Cuprija", "Ivo Andric")

delete_book_by_name("The Fog")
print(books)


book = find_book_by_name("The Fog")
print(book)
