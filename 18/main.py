import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='python_db_test',
)

if connection.open:
    print("Connection to DB established")
else:
    print("Not Connected!")

cursor = connection.cursor()

# primer za query
cursor.execute("INSERT INTO users (username, password, age) VALUES ('Branislav', '12344321', '44')")
connection.commit()
