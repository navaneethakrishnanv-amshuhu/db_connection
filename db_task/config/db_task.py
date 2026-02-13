import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG
import sys

print("🚀 db_task.py started")

print("Using configuration:")
print(f"  host: {DB_CONFIG['host']}")
print(f"  username: {DB_CONFIG['username']}")
print(f"  database: {DB_CONFIG['database']}")
print(f"  port: {DB_CONFIG['port']}")

connection = None

try:
    print("\n🔌 Attempting to connect...", flush=True)

    connection = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["username"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        port=DB_CONFIG["port"],
        connection_timeout=3,   # ⬅ hard timeout
        use_pure=True           # ⬅ CRITICAL on Windows
    )

    print("🔎 Connection call returned", flush=True)

    if connection.is_connected():
        print("✅ SUCCESS: Connected to MySQL")

except Error as e:
    print("❌ MySQL Error:", e)
    sys.exit(1)

except Exception as e:
    print("❌ Python Error:", e)
    sys.exit(1)

finally:
    if connection and connection.is_connected():
        connection.close()
        print("🔌 Connection closed")
