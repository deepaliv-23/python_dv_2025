from db_conn import get_connection

def view_data():
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        if rows:
            print("📄 All Users:")
            for row in rows:
                print(row)
        else:
            print("⚠️ No records found.")
    except Exception as e:
        print(f"❌ Error viewing data: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
