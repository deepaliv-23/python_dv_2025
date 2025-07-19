from db_conn import get_connection

def update_data():
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        query = "UPDATE users SET age = %s WHERE name = %s"
        cursor.execute(query, (30, "Namrata"))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ Data updated!")
        else:
            print("⚠️ No matching record found to update.")
    except Exception as e:
        print(f"❌ Error updating data: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
