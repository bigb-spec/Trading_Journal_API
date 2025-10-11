import time
import MySQLdb
from MySQLdb import OperationalError

print("Waiting for MySQL to be ready...")
while True:
    try:
        conn = MySQLdb.connect(
            host="mysql",
            user="trading_user",
            passwd="trading_password",
            db="trading_db",
            port=3306
        )
        conn.close()
        print("✅ MySQL is ready!")
        break
    except OperationalError:
        print("⏳ Database not ready yet, retrying in 2 seconds...")
        time.sleep(2)
