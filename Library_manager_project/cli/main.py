# Name: Tanisq Kumar
# Date: October 11, 2025
# Project Title: Library Inventory Manager CLI
# Course: Programming for Problem Solving using Python
"""
Command Line Interface for Library Inventory Manager
"""

import sys
import os

# Add parent directory to path to import library_manager
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library_manager import Book, LibraryInventory


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Print the application header."""
    print("=" * 60)
    print(" " * 15 + "LIBRARY INVENTORY MANAGER")
    print("=" * 60)
    print()


def print_menu():
    """Display the main menu."""
    print("\n" + "─" * 60)
    print("MAIN MENU")
    print("─" * 60)
    print("1. Add New Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book by Title")
    print("6. Search Book by ISBN")
    print("7. Search Book by Author")
    print("8. View Statistics")
    print("9. Exit")
    print("─" * 60)


def get_valid_input(prompt, input_type=str, allow_empty=False):
    """
    Get validated input from user.
    
    Args:
        prompt (str): Prompt message
        input_type (type): Expected input type
        allow_empty (bool): Whether to allow empty input
        
    Returns:
        Input value or None if invalid
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            if not user_input and not allow_empty:
                print(" Input cannot be empty. Please try again.")
                continue
            
            if user_input or allow_empty:
                if input_type == int:
                    return int(user_input)
                return user_input
                
        except ValueError:
            print(f" Invalid input. Expected {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\n\n  Operation cancelled by user.")
            return None


def add_book_cli(inventory):
    """Add a new book through CLI."""
    print("\n" + "─" * 60)
    print("ADD NEW BOOK")
    print("─" * 60)
    
    title = get_valid_input("Enter book title: ")
    if not title:
        return
    
    author = get_valid_input("Enter author name: ")
    if not author:
        return
    
    isbn = get_valid_input("Enter ISBN: ")
    if not isbn:
        return
    
    try:
        book = Book(title, author, isbn)
        if inventory.add_book(book):
            print(f"\n  Book '{title}' added successfully!")
        else:
            print(f"\n  Book with ISBN {isbn} already exists!")
    except Exception as e:
        print(f"\n  Error adding book: {e}")

def issue_book_cli(inventory):
    """Issue a book through CLI."""
    print("\n" + "─" * 60)
    print("ISSUE BOOK")
    print("─" * 60)
    
    isbn = get_valid_input("Enter ISBN of the book to issue: ")
    if not isbn:
        return
    
    try:
        if inventory.issue_book(isbn):
            print(f"\n✅ Book with ISBN {isbn} issued successfully!")
        else:
            print(f"\n❌ Could not issue book. It may already be issued or not found.")
    except Exception as e:
        print(f"\n❌ Error issuing book: {e}")


def return_book_cli(inventory):
    """Return a book through CLI."""
    print("\n" + "─" * 60)
    print("RETURN BOOK")
    print("─" * 60)
    
    isbn = get_valid_input("Enter ISBN of the book to return: ")
    if not isbn:
        return
    
    try:
        if inventory.return_book(isbn):
            print(f"\n✅ Book with ISBN {isbn} returned successfully!")
        else:
            print(f"\n❌ Could not return book. It may not be issued or not found.")
    except Exception as e:
        print(f"\n❌ Error returning book: {e}")


def display_books(books, message="BOOKS IN INVENTORY"):
    """Display a list of books."""
    print("\n" + "─" * 60)
    print(message)
    print("─" * 60)
    
    if not books:
        print("📚 No books found.")
        return
    
    for i, book in enumerate(books, 1):
        status_icon = "✅" if book.is_available() else "📤"
        print(f"\n{i}. {status_icon} {book}")


def view_all_books_cli(inventory):
    """View all books through CLI."""
    try:
        books = inventory.display_all()
        display_books(books)
    except Exception as e:
        print(f"\n❌ Error displaying books: {e}")


def search_by_title_cli(inventory):
    """Search books by title through CLI."""
    print("\n" + "─" * 60)
    print("SEARCH BY TITLE")
    print("─" * 60)
    
    title = get_valid_input("Enter title to search: ")
    if not title:
        return
    
    try:
        books = inventory.search_by_title(title)
        display_books(books, f"SEARCH RESULTS FOR '{title}'")
    except Exception as e:
        print(f"\n❌ Error searching books: {e}")


def search_by_isbn_cli(inventory):
    """Search book by ISBN through CLI."""
    print("\n" + "─" * 60)
    print("SEARCH BY ISBN")
    print("─" * 60)
    
    isbn = get_valid_input("Enter ISBN to search: ")
    if not isbn:
        return
    
    try:
        book = inventory.search_by_isbn(isbn)
        if book:
            display_books([book], f"BOOK WITH ISBN '{isbn}'")
        else:
            print(f"\n📚 No book found with ISBN '{isbn}'.")
    except Exception as e:
        print(f"\n❌ Error searching book: {e}")


def search_by_author_cli(inventory):
    """Search books by author through CLI."""
    print("\n" + "─" * 60)
    print("SEARCH BY AUTHOR")
    print("─" * 60)
    
    author = get_valid_input("Enter author name to search: ")
    if not author:
        return
    
    try:
        books = inventory.search_by_author(author)
        display_books(books, f"BOOKS BY '{author}'")
    except Exception as e:
        print(f"\n❌ Error searching books: {e}")


def view_statistics_cli(inventory):
    """View inventory statistics through CLI."""
    print("\n" + "─" * 60)
    print("INVENTORY STATISTICS")
    print("─" * 60)
    
    try:
        stats = inventory.get_statistics()
        print(f"\n📊 Total Books: {stats['total']}")
        print(f"✅ Available: {stats['available']}")
        print(f"📤 Issued: {stats['issued']}")
    except Exception as e:
        print(f"\n❌ Error fetching statistics: {e}")


def main():
    """Main function to run the CLI application."""
    try:
        inventory = LibraryInventory()
        
        while True:
            print_header()
            print_menu()
            
            choice = get_valid_input("\nEnter your choice (1-9): ")
            
            if not choice:
                continue
            
            if choice == '1':
                add_book_cli(inventory)
            elif choice == '2':
                issue_book_cli(inventory)
            elif choice == '3':
                return_book_cli(inventory)
            elif choice == '4':
                view_all_books_cli(inventory)
            elif choice == '5':
                search_by_title_cli(inventory)
            elif choice == '6':
                search_by_isbn_cli(inventory)
            elif choice == '7':
                search_by_author_cli(inventory)
            elif choice == '8':
                view_statistics_cli(inventory)
            elif choice == '9':
                print("\n👋 Thank you for using Library Inventory Manager!")
                print("Goodbye!\n")
                sys.exit(0)
            else:
                print("\n❌ Invalid choice. Please select 1-9.")
            
            input("\nPress Enter to continue...")
            clear_screen()
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Application interrupted by user.")
        print("👋 Goodbye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
