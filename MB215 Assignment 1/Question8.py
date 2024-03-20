import os

def add_book(filename, title, author, year):
    with open(filename, 'a') as file:
        file.write(f"{title}, by {author}, Published in {year}\n")
    print("Book added successfully!\n")

def list_all_books(filename):
    try:
        with open(filename, 'r') as file:
            print("Library Catalogue:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No catalogue found. A new catalogue will be created when you add a book.\n")

def search_for_book(filename, search_term):
    try:
        with open(filename, 'r') as file:
            catalogue = file.readlines()
        found_books = [book for book in catalogue if search_term.lower() in book.lower()]
        if found_books:
            print("\nSearch Results:")
            for book in found_books:
                print(book.strip())
        else:
            print("No matching books found.\n")
    except FileNotFoundError:
        print("No catalogue to search from. Please add a book first.\n")

def remove_book(filename, title):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        with open(filename, 'w') as file:
            book_removed = False
            for line in lines:
                if title.lower() not in line.lower():
                    file.write(line)
                else:
                    book_removed = True
            if book_removed:
                print("Book removed successfully!\n")
            else:
                print("Book not found in the catalogue.\n")
    except FileNotFoundError:
        print("No catalogue to remove from. Please add a book first.\n")

# Main program function
def main():
    filename = 'library_catalogue.txt'
    if not os.path.isfile(filename):
        print("Welcome to your Personal Library Catalogue!")
        print("No existing catalogue found. A new one will be created for you.\n")
        open(filename, 'w').close()

    while True:
        print("Please choose an option:")
        print("1 - Add a New Book")
        print("2 - List All Books")
        print("3 - Search for a Book")
        print("4 - Remove a Book")
        print("0 - Exit\n")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("\nEnter the book title: ")
            author = input("Enter the author's name: ")
            year = input("Enter the year of publication: ")
            add_book(filename, title, author, year)
        elif choice == "2":
            list_all_books(filename)
        elif choice == "3":
            search_term = input("\nEnter a title or author to search for: ")
            search_for_book(filename, search_term)
        elif choice == "4":
            title = input("\nEnter the title of the book to remove: ")
            remove_book(filename, title)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()