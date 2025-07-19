import mysql.connector
from mysql.connector import IntegrityError
from db_conn import get_connection

def insert_data():
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        data = [
            ("Namrata", "namrata@example.com", 25),
            ("Amit", "amit@example.com", 28),
            ("Priya", "priya@example.com", 22)
        ]
        cursor.executemany(query, data)
        conn.commit()
        print("✅ Data inserted!")
    except mysql.connector.IntegrityError as e:
        print(f"⚠️ Duplicate or constraint error: {e}")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
