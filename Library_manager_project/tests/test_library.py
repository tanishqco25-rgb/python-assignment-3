"""
Unit tests for Library Inventory Manager
"""

import unittest
import json
import os
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library_manager import Book, LibraryInventory


class TestBook(unittest.TestCase):
    """Test cases for the Book class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.book = Book("Test Book", "Test Author", "1234567890")
    
    def test_book_creation(self):
        """Test book creation with default status."""
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.isbn, "1234567890")
        self.assertEqual(self.book.status, "available")
    
    def test_book_str(self):
        """Test string representation of book."""
        expected = "Title: Test Book | Author: Test Author | ISBN: 1234567890 | Status: available"
        self.assertEqual(str(self.book), expected)
    
    def test_book_to_dict(self):
        """Test conversion to dictionary."""
        expected = {
            'title': "Test Book",
            'author': "Test Author",
            'isbn': "1234567890",
            'status': "available"
        }
        self.assertEqual(self.book.to_dict(), expected)
    
    def test_issue_book(self):
        """Test issuing an available book."""
        result = self.book.issue()
        self.assertTrue(result)
        self.assertEqual(self.book.status, "issued")
    
    def test_issue_already_issued_book(self):
        """Test issuing an already issued book."""
        self.book.issue()
        result = self.book.issue()
        self.assertFalse(result)
    
    def test_return_book(self):
        """Test returning an issued book."""
        self.book.issue()
        result = self.book.return_book()
        self.assertTrue(result)
        self.assertEqual(self.book.status, "available")
    
    def test_return_available_book(self):
        """Test returning an available book."""
        result = self.book.return_book()
        self.assertFalse(result)
    
    def test_is_available(self):
        """Test checking book availability."""
        self.assertTrue(self.book.is_available())
        self.book.issue()
        self.assertFalse(self.book.is_available())


class TestLibraryInventory(unittest.TestCase):
    """Test cases for the LibraryInventory class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_catalog = "test_catalog.json"
        self.inventory = LibraryInventory(self.test_catalog)
        self.inventory.books = []  # Clear any existing books
    
    def tearDown(self):
        """Clean up test files."""
        if Path(self.test_catalog).exists():
            os.remove(self.test_catalog)
        if Path(self.test_catalog + '.backup').exists():
            os.remove(self.test_catalog + '.backup')
    
    def test_add_book(self):
        """Test adding a book to inventory."""
        book = Book("Python Programming", "John Doe", "1111111111")
        result = self.inventory.add_book(book)
        self.assertTrue(result)
        self.assertEqual(len(self.inventory.books), 1)
    
    def test_add_duplicate_isbn(self):
        """Test adding a book with duplicate ISBN."""
        book1 = Book("Book One", "Author One", "2222222222")
        book2 = Book("Book Two", "Author Two", "2222222222")
        self.inventory.add_book(book1)
        result = self.inventory.add_book(book2)
        self.assertFalse(result)
        self.assertEqual(len(self.inventory.books), 1)
    
    def test_search_by_title(self):
        """Test searching books by title."""
        book1 = Book("Python Programming", "Author One", "3333333333")
        book2 = Book("Java Programming", "Author Two", "4444444444")
        self.inventory.add_book(book1)
        self.inventory.add_book(book2)
        
        results = self.inventory.search_by_title("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Python Programming")
    
    def test_search_by_isbn(self):
        """Test searching book by ISBN."""
        book = Book("Data Science", "Jane Smith", "5555555555")
        self.inventory.add_book(book)
        
        result = self.inventory.search_by_isbn("5555555555")
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Data Science")
    
    def test_search_by_author(self):
        """Test searching books by author."""
        book1 = Book("Book One", "John Doe", "6666666666")
        book2 = Book("Book Two", "John Doe", "7777777777")
        self.inventory.add_book(book1)
        self.inventory.add_book(book2)
        
        results = self.inventory.search_by_author("John")
        self.assertEqual(len(results), 2)
    
    def test_issue_book(self):
        """Test issuing a book."""
        book = Book("Test Book", "Test Author", "8888888888")
        self.inventory.add_book(book)
        
        result = self.inventory.issue_book("8888888888")
        self.assertTrue(result)
        self.assertEqual(book.status, "issued")
    
    def test_return_book(self):
        """Test returning a book."""
        book = Book("Test Book", "Test Author", "9999999999")
        self.inventory.add_book(book)
        self.inventory.issue_book("9999999999")
        
        result = self.inventory.return_book("9999999999")
        self.assertTrue(result)
        self.assertEqual(book.status, "available")
    
    def test_save_and_load_catalog(self):
        """Test saving and loading catalog."""
        book = Book("Persistent Book", "Author", "1010101010")
        self.inventory.add_book(book)
        
        # Create new inventory instance
        new_inventory = LibraryInventory(self.test_catalog)
        self.assertEqual(len(new_inventory.books), 1)
        self.assertEqual(new_inventory.books[0].title, "Persistent Book")
    
    def test_get_statistics(self):
        """Test getting inventory statistics."""
        book1 = Book("Book 1", "Author 1", "1212121212")
        book2 = Book("Book 2", "Author 2", "1313131313")
        self.inventory.add_book(book1)
        self.inventory.add_book(book2)
        self.inventory.issue_book("1212121212")
        
        stats = self.inventory.get_statistics()
        self.assertEqual(stats['total'], 2)
        self.assertEqual(stats['available'], 1)
        self.assertEqual(stats['issued'], 1)


def run_tests():
    """Run all tests."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestBook))
    suite.addTests(loader.loadTestsFromTestCase(TestLibraryInventory))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
