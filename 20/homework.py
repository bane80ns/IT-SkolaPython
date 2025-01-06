from models.db_con import connection
from models.book import *
from models.user import *
import time

# dob = generate_random_dob()
# # print(dob)
#
# genre = generate_random_genre()
# # print(genre)
#
# author = generate_random_author()
# # print(author)
#
# book_title = generate_book_title(genre, author)
# # print(book_title)
#
# author_id = insert_user(connection, author, dob)
# insert_book(connection, book_title, genre, author_id)
#
# print(book_title, author)
#
# time.sleep(0.3)

# books  = get_all_books(connection)

# for book in books:
#     print(book['name'])





choice = None
while choice is None or choice == "":
    choice = input("What do you want to do?\n 1. Create Random book\n 2. Show books\n 3. Search for book by ID\n 4. Remove book: \nq - Quit\n")

    if choice == "1":
        dob = generate_random_dob()
        # print(dob)

        genre = generate_random_genre()
        # print(genre)

        author = generate_random_author()
        # print(author)

        book_title = generate_book_title(genre, author)
        # print(book_title)

        author_id = insert_user(connection, author, dob)
        insert_book(connection, book_title, genre, author_id)

        print(book_title, author)
        choice = None



    elif choice == "2":
        books = get_all_books(connection)
        for book in books:
            print(book)
        print("\n")
        choice = None


    elif choice == "3":
        book_id = None
        while book_id is None:
            book_id = int(input("\nEnter ID of the book you wanna search for: "))
            book = get_book_by_id(connection, book_id)
            if book is not None:
                print(book, "\n")
            else:
                print("Id not found or something went wrong...\n")
        choice = None


    elif choice == "4":
        book_id = None
        while book_id is None:
            book_id = int(input("\nEnter ID of the book you wanna remove: "))
            delete_book_by_id(connection, book_id)

        choice = None

    elif choice == "q":
        print("Goodbye...")
        break
