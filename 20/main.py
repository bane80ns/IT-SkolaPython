from faker import Faker
import random
from datetime import datetime

faker = Faker()
dob = faker.date_between(start_date=datetime(1950, 1, 1), end_date=datetime(1980, 3, 11))

def generate_random_dob():
    return faker.date_between(start_date=datetime(1950, 1, 1), end_date=datetime(1980, 3, 11))

def generate_random_genre():
    genres = ["Mystery", "Adventure", "Fantasy", "Love Story", ""]
    return random.choice(genres)



def generate_book_title(con):
    genres = ["Mystery", "Adventure", "Fantasy"]
    adjectives = ["Dark", "Forbidden", "Mysterious", "Hidden", "Eternal"]
    nouns = ["Secrets", "Kingdom", "Journey", "Love", "Shadow"]

    genre = random.choice(genres)
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    author_name = faker.name()

    book_name = f"{adjective} {noun}: A {genre} story by {author_name}"
    dob = faker.date_between(start_date=datetime (1950, 1, 1) , end_date=datetime (1980,3,11))


    cursor = con.cursor()

    query = "INSERT INTO books (name, category, author) VALUES (%s, %s, %s)"
    cursor.execute(query, (book_name, genre, author_name))

    user_query = "INSERT INTO users (name, dob) VALUES (%s, %s)"
    cursor.execute(user_query, (author_name, dob))

    con.commit()
    cursor.close()

# generate_book_title(connection)

def insert_user(con, name, dob):
    cursor = con.cursor()

    user_query = "INSERT INTO users (name, dob) VALUES (%s, %s)"
    cursor.execute(user_query, (name, dob))
    con.commit()
    cursor.close()

def insert_book(con, name, genre, author):
    cursor = con.cursor()

    query = "INSERT INTO books (name, category, author) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, category))
    con.commit()
    cursor.close()