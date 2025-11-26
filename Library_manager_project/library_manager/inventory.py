"""
Library Inventory Manager module
"""

import json
import logging
from pathlib import Path
from .book import Book

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('library_manager.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class LibraryInventory:
    """
    Manages the library's book inventory.
    
    Attributes:
        books (list): List of Book objects in the inventory
        catalog_file (Path): Path to the JSON catalog file
    """
    
    def __init__(self, catalog_file="library_catalog.json"):
        """
        Initialize the LibraryInventory.
        
        Args:
            catalog_file (str): Path to the JSON catalog file
        """
        self.books = []
        self.catalog_file = Path(catalog_file)
        self.load_catalog()
        logger.info("Library Inventory initialized")
    
    def add_book(self, book):
        """
        Add a book to the inventory.
        
        Args:
            book (Book): Book object to add
            
        Returns:
            bool: True if book was added successfully
        """
        try:
            # Check if ISBN already exists
            if any(b.isbn == book.isbn for b in self.books):
                logger.warning(f"Book with ISBN {book.isbn} already exists")
                return False
            
            self.books.append(book)
            self.save_catalog()
            logger.info(f"Book added: {book.title} (ISBN: {book.isbn})")
            return True
        except Exception as e:
            logger.error(f"Error adding book: {e}")
            return False
    
    def search_by_title(self, title):
        """
        Search for books by title (case-insensitive partial match).
        
        Args:
            title (str): Title to search for
            
        Returns:
            list: List of matching Book objects
        """
        try:
            results = [book for book in self.books 
                      if title.lower() in book.title.lower()]
            logger.info(f"Search by title '{title}': {len(results)} results found")
            return results
        except Exception as e:
            logger.error(f"Error searching by title: {e}")
            return []
    
    def search_by_isbn(self, isbn):
        """
        Search for a book by ISBN.
        
        Args:
            isbn (str): ISBN to search for
            
        Returns:
            Book or None: Book object if found, None otherwise
        """
        try:
            for book in self.books:
                if book.isbn == isbn:
                    logger.info(f"Book found by ISBN {isbn}")
                    return book
            logger.info(f"No book found with ISBN {isbn}")
            return None
        except Exception as e:
            logger.error(f"Error searching by ISBN: {e}")
            return None
    
    def search_by_author(self, author):
        """
        Search for books by author (case-insensitive partial match).
        
        Args:
            author (str): Author name to search for
            
        Returns:
            list: List of matching Book objects
        """
        try:
            results = [book for book in self.books 
                      if author.lower() in book.author.lower()]
            logger.info(f"Search by author '{author}': {len(results)} results found")
            return results
        except Exception as e:
            logger.error(f"Error searching by author: {e}")
            return []
    
    def display_all(self):
        """
        Display all books in the inventory.
        
        Returns:
            list: List of all Book objects
        """
        return self.books
    
    def save_catalog(self):
        """
        Save the inventory to a JSON file.
        
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            books_data = [book.to_dict() for book in self.books]
            with open(self.catalog_file, 'w', encoding='utf-8') as file:
                json.dump(books_data, file, indent=4, ensure_ascii=False)
            logger.info(f"Catalog saved to {self.catalog_file}")
            return True
        except IOError as e:
            logger.error(f"IO Error saving catalog: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error saving catalog: {e}")
            return False
    
    def load_catalog(self):
        """
        Load the inventory from a JSON file.
        
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            if not self.catalog_file.exists():
                logger.warning(f"Catalog file {self.catalog_file} not found. Creating new catalog.")
                self.books = []
                self.save_catalog()
                return True
            
            with open(self.catalog_file, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                self.books = [Book(**book_dict) for book_dict in books_data]
            
            logger.info(f"Catalog loaded: {len(self.books)} books")
            return True
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}. Creating backup and new catalog.")
            # Create backup of corrupted file
            if self.catalog_file.exists():
                backup_file = self.catalog_file.with_suffix('.json.backup')
                self.catalog_file.rename(backup_file)
            self.books = []
            self.save_catalog()
            return False
            
        except IOError as e:
            logger.error(f"IO Error loading catalog: {e}")
            self.books = []
            return False
            
        except Exception as e:
            logger.error(f"Unexpected error loading catalog: {e}")
            self.books = []
            return False
    
    def issue_book(self, isbn):
        """
        Issue a book by ISBN.
        
        Args:
            isbn (str): ISBN of the book to issue
            
        Returns:
            bool: True if book was issued, False otherwise
        """
        try:
            book = self.search_by_isbn(isbn)
            if book:
                if book.issue():
                    self.save_catalog()
                    logger.info(f"Book issued: {book.title} (ISBN: {isbn})")
                    return True
                else:
                    logger.warning(f"Book already issued: {book.title} (ISBN: {isbn})")
                    return False
            else:
                logger.warning(f"Book not found with ISBN: {isbn}")
                return False
        except Exception as e:
            logger.error(f"Error issuing book: {e}")
            return False
    
    def return_book(self, isbn):
        """
        Return a book by ISBN.
        
        Args:
            isbn (str): ISBN of the book to return
            
        Returns:
            bool: True if book was returned, False otherwise
        """
        try:
            book = self.search_by_isbn(isbn)
            if book:
                if book.return_book():
                    self.save_catalog()
                    logger.info(f"Book returned: {book.title} (ISBN: {isbn})")
                    return True
                else:
                    logger.warning(f"Book was not issued: {book.title} (ISBN: {isbn})")
                    return False
            else:
                logger.warning(f"Book not found with ISBN: {isbn}")
                return False
        except Exception as e:
            logger.error(f"Error returning book: {e}")
            return False
    
    def get_statistics(self):
        """
        Get inventory statistics.
        
        Returns:
            dict: Dictionary with statistics
        """
        total = len(self.books)
        available = sum(1 for book in self.books if book.is_available())
        issued = total - available
        
        return {
            'total': total,
            'available': available,
            'issued': issued
        }
