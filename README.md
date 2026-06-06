# Library Management System

A simple command-line Library Management System built using Python and MySQL.

## Features

- Add books
- View all books
- Search books
- Store data in a MySQL database

## Technologies Used

- Python
- MySQL
- mysql-connector-python
- Git
- GitHub

## Database Setup

Create the database:

```sql
CREATE DATABASE library_db;
USE library_db;
```

Create the books table:

```sql
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(100),
    author_name VARCHAR(100)
);
```

## Installation

Install the required package:

```bash
pip install mysql-connector-python
```

## Configuration

Update the database connection details in `db.py`:

```python
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="library_db"
    )
```

## Run the Project

```bash
python library.py
```

## Project Structure

```text
LibraryManagementSystem
│
├── library.py
├── db.py
├── README.md
└── .gitignore
```

## Future Improvements

- Delete books
- Update book details
- Book issue and return system
- User authentication
- GUI using Tkinter

## Author

Praveen Yeluri