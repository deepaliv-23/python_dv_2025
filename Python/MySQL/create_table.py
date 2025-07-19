from db_conn import get_connection

def create_table():
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100),
                age INT
            )
        """)
        conn.commit()
        print("✅ Table created!")
    except Exception as e:
        print(f"❌ Error creating table: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()