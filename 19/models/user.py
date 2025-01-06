


def insert_user(con, author, date_of_birth):
    cursor = con.cursor()
    user_query = "INSERT INTO users (name, dob) VALUES (%s, %s)"

    cursor.execute(user_query, (author, date_of_birth))
    con.commit()
    cursor.close()
    return cursor.lastrowid