import pymysql

class Db:
    def __init__(self):

        db_name = "oop2_test"

        self.connection = pymysql.connect(
            host='localhost',  # localhost - Local PC, or 127.0.0.1 (This field is for DB IP address)
            user='root',  # username created for accessing DB (Database)
            password='root',  # password created for accessing DB
            database=db_name,  # DB name
            cursorclass=pymysql.cursors.DictCursor
            #   port=xxxx # Port which we use for connecting to DB (in our case not needed)
        )

        # DB Check if its connected and ready for work.
        if self.connection.open:
            print(f"Connection to DB ***** {db_name} ***** established.\nYou may proceed...\n")
        else:
            print("DB connection failed!\nCheck your connection and try again.\n")

