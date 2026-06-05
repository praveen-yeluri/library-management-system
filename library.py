books = []

while True:
    print("\n===== Library Management =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_name = input("Enter book name: ")
        author_name = input("Enter author name: ")

        books.append({
            "book": book_name,
            "author": author_name
        })

        print("Book added successfully!")

    elif choice == "2":
        print("\nBooks in Library:")

        for book in books:
            print(f"Book: {book['book']}")
            print(f"Author: {book['author']}")
            print("-" * 20)

    elif choice == "3":
        search = input("Enter book name to search: ")

        found = False

        for book in books:
            if book["book"].lower() == search.lower():
                print("\nBook Found!")
                print(f"Book: {book['book']}")
                print(f"Author: {book['author']}")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")