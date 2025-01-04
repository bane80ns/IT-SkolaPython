from faker import Faker
import random
from datetime import datetime
from db_con import connection
faker = Faker()


def insert_user(con, author, date_of_birth):
    cursor = con.cursor()

    user_query = "INSERT INTO users (name, dob) VALUES (%s, %s)"
    cursor.execute(user_query, (author, date_of_birth))
    con.commit()
    cursor.close()


def insert_book(con, book_title, genre, author):
    cursor = con.cursor()

    query = "INSERT INTO books (name, category, author) VALUES (%s, %s, %s)"
    cursor.execute(query, (book_title, genre, author))
    con.commit()
    cursor.close()


def generate_random_dob():
    return faker.date_between(start_date=datetime(1950, 1, 1), end_date=datetime(1980, 3, 11))


def generate_random_genre():
    genres = ["Mystery", "Adventure", "Fantasy", "Horror"]
    return random.choice(genres)


def generate_random_author():
    return faker.name()


def generate_book_title(book_genre, book_author):
    nouns = ["Secrets", "Kingdom", "Journey", "Love", "Shadow"]
    adjectives = ["Dark", "Forbidden", "Mysterious", "Hidden", "Eternal"]
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    return (f"{adjective} {noun}: A {book_genre} story by {book_author}")


dob = generate_random_dob()
genre = generate_random_genre()
author = generate_random_author()
book_title = generate_book_title(genre, author)

insert_user(connection, author, dob)
insert_book(connection, book_title, genre, author)





print(dob, genre, author)
print(book_title)