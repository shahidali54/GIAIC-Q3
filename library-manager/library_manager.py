import json
import os
import csv

library = []
library_file = "library.json"

def load_library():
    global library
    if os.path.exists(library_file):
        with open(library_file, "r") as file:
            try:
                library = json.load(file)
            except json.JSONDecodeError:
                library = []
    else:
        library = []

def save_library():
    with open(library_file, "w") as file:
        json.dump(library, file, indent=4)

def add_book():
    print("\n--- Add a Book ---")
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    try:
        year = int(input("Enter Publication Year: ").strip())
    except ValueError:
        print("Invalid year. Please enter a valid integer.")
        return
    genre = input("Enter Genre: ").strip()
    read_status_input = input("Have you read this book? (y/n): ").strip().lower()
    read_status = True if read_status_input == 'y' else False

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read_status
    }

    library.append(book)
    save_library()
    print(f"Book '{title}' added successfully!")

def remove_book():
    print("\n--- Remove a Book ---")
    title = input("Enter Title of the book to remove: ").strip()
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            save_library()
            print(f"Book '{title}' removed successfully!")
            return
    print(f"Book '{title}' not found in library.")

def edit_book():
    print("\n--- Edit Book Details ---")
    title = input("Enter Title of the book to edit: ").strip()
    for book in library:
        if book["Title"].lower() == title.lower():
            print("Leave blank to keep current value.")
            new_title = input(f"New Title ({book['Title']}): ").strip()
            new_author = input(f"New Author ({book['Author']}): ").strip()
            new_year_input = input(f"New Year ({book['Year']}): ").strip()
            new_genre = input(f"New Genre ({book['Genre']}): ").strip()
            new_read_status = input(f"Read Status ({'Yes' if book['Read'] else 'No'}), (y/n): ").strip().lower()

            if new_title:
                book["Title"] = new_title
            if new_author:
                book["Author"] = new_author
            if new_year_input:
                try:
                    book["Year"] = int(new_year_input)
                except ValueError:
                    print("Invalid year, keeping original.")
            if new_genre:
                book["Genre"] = new_genre
            if new_read_status == 'y':
                book["Read"] = True
            elif new_read_status == 'n':
                book["Read"] = False

            save_library()
            print("Book details updated successfully!")
            return
    print(f"Book '{title}' not found.")

def search_book():
    print("\n--- Search a Book ---")
    keyword = input("Enter Title or Author to search: ").strip().lower()
    found_books = [book for book in library if keyword in book["Title"].lower() or keyword in book["Author"].lower()]
    if found_books:
        print("\nFound Books:")
        for book in found_books:
            display_book(book)
    else:
        print("No matching books found.")

def filter_by_genre():
    print("\n--- Filter by Genre ---")
    genre_input = input("Enter Genre to filter: ").strip().lower()
    genre_books = [book for book in library if genre_input in book["Genre"].lower()]
    if genre_books:
        print(f"\nBooks in Genre '{genre_input}':")
        for book in genre_books:
            display_book(book)
    else:
        print("No books found in this genre.")

def display_all_books():
    print("\n--- All Books ---")
    if not library:
        print("Library is empty.")
    else:
        for book in library:
            display_book(book)

def display_book(book):
    print(f"\nTitle: {book['Title']}")
    print(f"Author: {book['Author']}")
    print(f"Year: {book['Year']}")
    print(f"Genre: {book['Genre']}")
    print(f"Read: {'Yes' if book['Read'] else 'No'}")

def display_statistics():
    print("\n--- Library Statistics ---")
    total_books = len(library)
    if total_books == 0:
        print("Library is empty.")
        return
    read_books = sum(1 for book in library if book["Read"])
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books} ({percentage_read:.2f}%)")

def export_to_csv():
    print("\n--- Exporting to CSV ---")
    csv_file = "library_export.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Year", "Genre", "Read"])
        writer.writeheader()
        for book in library:
            writer.writerow(book)
    print(f"Library exported successfully to '{csv_file}'!")

def menu():
    while True:
        print("\n===== Personal Library Manager =====")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Edit book details")
        print("4. Search for a book")
        print("5. Filter by genre")
        print("6. Display all books")
        print("7. Display statistics")
        print("8. Export to CSV")
        print("9. Exit")
        choice = input("Select an option (1-9): ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            edit_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            filter_by_genre()
        elif choice == '6':
            display_all_books()
        elif choice == '7':
            display_statistics()
        elif choice == '8':
            export_to_csv()
        elif choice == '9':
            print("Saving and exiting program... Goodbye!")
            save_library()
            break
        else:
            print("Invalid option! Please select a number between 1 and 9.")

if __name__ == "__main__":
    load_library()
    menu()
