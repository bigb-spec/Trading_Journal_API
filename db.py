from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="journal_user",
        password="journal_pass",
        database = "trading_journal"
    ) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM trading_journal")
        print(cursor.fetchall())
    pass
except Error as e:
    print(e)