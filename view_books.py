from db import connect_db

conn = connect_db()
cursor = conn.cursor()

cursor.execute("SELECT * FROM books")

books = cursor.fetchall()

for book in books:
    print(f"ID: {book[0]}")
    print(f"Book: {book[1]}")
    print(f"Author: {book[2]}")
    print("-" * 20)

conn.close()