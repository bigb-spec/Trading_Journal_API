import time
import MySQLdb
import os

db_settings = {
    "host": os.getenv("DB_HOST", "mysql"),
    "user": os.getenv("DB_USER", "journal_user"),
    "passwd": os.getenv("DB_PASSWORD", "journal_pass123"),
    "database": os.getenv("DB_NAME", "trading_journal"),
}

print("⏳ Waiting for MySQL to be ready...")
while True:
    try:
        conn = MySQLdb.connect(**db_settings)
        conn.close()
        print("✅ MySQL is ready! Starting Django...")
        break
    except MySQLdb.OperationalError:
        time.sleep(2)
