# create_user -> name, password, age

import pymysql

db_name = "python_db_test"
connection = pymysql.connect(
    host='localhost', # localhost - Local PC, or 127.0.0.1 (This field is for DB IP address)
    user='root', # username created for accessing DB (Database)
    password='root', # password created for accessing DB
    database=db_name, # DB name
#   port=xxxx # Port which we use for connecting to DB (in our case not needed)
)

# DB Check if its connected and ready for work.
if connection.open:
    print(f"Connection to DB ***** {db_name} ***** established.\nYou may proceed...\n")
else:
    print("DB connection failed!\nCheck your connection and try again.\n")

# cursor is variable we use for manipulating DB query's
# cursor = connection.cursor() Its now wise using cursor as global.


def create_user(con, username, password, age):
    cursor = con.cursor()

    db_query = "INSERT INTO users (username, password, age) VALUES (%s, %s, %s)"
    cursor.execute(db_query, (username, password, age)) # Adding query to cursor var which we wanna insert into DB
    con.commit() # Writing query into DB
    cursor.close() # Closing cursor connection to DB!
    print("User created successfully!\n")

# create_user(connection,"bane", "2130", 39) # example for create_user def
