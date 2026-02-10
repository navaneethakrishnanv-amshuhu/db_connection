"""
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


def connect_to_database():
    #Establishes a connection to the MySQL database using credentials from config.py
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["username"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
            port=DB_CONFIG["port"]
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("=" * 50)
            print("✅ CONNECTION SUCCESSFUL!")
            print("=" * 50)
            print(f"Connected to MySQL Server version: {db_info}")
            
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            database_name = cursor.fetchone()[0]
            print(f"Connected to database: {database_name}")
            print("=" * 50)
            
            return connection
            
    except Error as e:
        print("=" * 50)
        print("❌ CONNECTION FAILED!")
        print("=" * 50)
        print(f"Error: {e}")
        print("=" * 50)
        return None


def close_connection(connection):
    # Closes the database connection
    if connection and connection.is_connected():
        connection.close()
        print("🔌 MySQL connection closed.")


# Main execution
if __name__ == "__main__":
    print("\nAttempting to connect to MySQL database...\n")
    
    # Establish connection
    conn = connect_to_database()
    
    # Close connection if it was successful
    if conn:
        close_connection(conn)
"""

"""
import sys

try:
    import mysql.connector
    from mysql.connector import Error
except ImportError:
    print("❌ mysql-connector-python is not installed!")
    print("Run: py -m pip install mysql-connector-python")
    sys.exit(1)

try:
    from config import DB_CONFIG
except ImportError:
    print("❌ Could not import config.py!")
    print("Make sure config.py is in the same folder as db_task.py")
    sys.exit(1)


def connect_to_database():
    Establishes a connection to the MySQL database using credentials from config.py

    connection = None
    
    print("Using configuration:")
    print(f"  Host: {DB_CONFIG['host']}")
    print(f"  Username: {DB_CONFIG['username']}")
    print(f"  Database: {DB_CONFIG['database']}")
    print(f"  Port: {DB_CONFIG['port']}")
    print("")
    
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["username"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
            port=DB_CONFIG["port"]
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("=" * 50)
            print("✅ CONNECTION SUCCESSFUL!")
            print("=" * 50)
            print(f"Connected to MySQL Server version: {db_info}")
            
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            database_name = cursor.fetchone()[0]
            print(f"Connected to database: {database_name}")
            print("=" * 50)
            
            return connection
            
    except Error as e:
        print("=" * 50)
        print("❌ CONNECTION FAILED!")
        print("=" * 50)
        print(f"Error: {e}")
        print("=" * 50)
        return None


def close_connection(connection):

    Closes the database connection

    if connection and connection.is_connected():
        connection.close()
        print("🔌 MySQL connection closed.")


# Main execution
if __name__ == "__main__":
    print("")
    print("Attempting to connect to MySQL database...")
    print("")
    
    # Establish connection
    conn = connect_to_database()
    
    # Close connection if it was successful
    if conn:
        close_connection(conn)
    else:
        print("")
        print("Troubleshooting tips:")
        print("1. Make sure MySQL server is running")
        print("2. Check your username and password in config.py")
        print("3. Make sure the database exists in MySQL")
    
    print("")
    input("Press Enter to exit...")
"""


import sys

print("Step 1: Starting script...")

try:
    import mysql.connector
    from mysql.connector import Error
    print("Step 2: mysql.connector imported successfully")
except Exception as e:
    print(f"Step 2 FAILED: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

try:
    from config import DB_CONFIG
    print("Step 3: config.py imported successfully")
except Exception as e:
    print(f"Step 3 FAILED: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

print("")
print("Using configuration:")
print(f"  Host: {DB_CONFIG['host']}")
print(f"  Username: {DB_CONFIG['username']}")
print(f"  Database: {DB_CONFIG['database']}")
print(f"  Port: {DB_CONFIG['port']}")
print("")

print("Step 4: Attempting to connect...")

try:
    connection = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["username"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        port=DB_CONFIG["port"]
    )
    print("Step 5: Connection object created")
    
    if connection.is_connected():
        print("")
        print("=" * 50)
        print("✅ CONNECTION SUCCESSFUL!")
        print("=" * 50)
        
        db_info = connection.get_server_info()
        print(f"MySQL Server version: {db_info}")
        
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        database_name = cursor.fetchone()[0]
        print(f"Connected to database: {database_name}")
        print("=" * 50)
        
        connection.close()
        print("Connection closed.")
    else:
        print("Connection object exists but is_connected() returned False")

except mysql.connector.Error as e:
    print("")
    print("=" * 50)
    print("❌ MySQL CONNECTION ERROR!")
    print("=" * 50)
    print(f"Error Code: {e.errno}")
    print(f"Error Message: {e.msg}")
    print("=" * 50)

except Exception as e:
    print("")
    print("=" * 50)
    print("❌ UNEXPECTED ERROR!")
    print("=" * 50)
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Message: {e}")
    print("=" * 50)

print("")
input("Press Enter to exit...")