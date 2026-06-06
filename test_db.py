from db import connect_db

conn = connect_db()
cursor = conn.cursor()

book = input("Enter book name: ")
author = input("Enter author name: ")

query = """
INSERT INTO books(book_name, author_name)
VALUES (%s, %s)
"""

cursor.execute(query, (book, author))
conn.commit()

print("Book added successfully!")

conn.close()