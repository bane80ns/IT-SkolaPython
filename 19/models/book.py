from datetime import datetime
from faker import Faker
import random
faker = Faker()


def generate_random_dob():
    return faker.date_between(start_date=datetime(1950, 1, 1), end_date=datetime(1980, 3, 11))


def generate_random_genre():
    genres = ["Mystery", "Adventure", "Fantasy", "Horror"]
    return random.choice(genres)


def generate_random_author():
    return faker.name()


def insert_book(con, book_title, genre, author):
    cursor = con.cursor()

    query = "INSERT INTO books (name, category, author) VALUES (%s, %s, %s)"
    cursor.execute(query, (book_title, genre, author))
    con.commit()
    cursor.close()


def generate_book_title(book_genre, book_author):
    nouns = ["Secrets", "Kingdom", "Journey", "Love", "Shadow"]
    adjectives = ["Dark", "Forbidden", "Mysterious", "Hidden", "Eternal"]
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    return (f"{adjective} {noun}: A {book_genre} story by {book_author}")


def get_all_books(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    return results
    con.commit()
    cursor.close()

def get_book_by_id(con, book_id):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM books WHERE id = %s", book_id)
    con.commit()
    results = cursor.fetchone()
    return results
    cursor.close()


def delete_book_by_id(con, book_id):
    cursor = con.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", book_id)
    con.commit()
    cursor.close()