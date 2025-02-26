import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Obama123",
        database="lecturer_retails"
    )
    print("Kết nối thành công!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Lỗi: {err}")
