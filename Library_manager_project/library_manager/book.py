"""
Book class module for Library Inventory Manager
"""

class Book:
    """
    Represents a book in the library inventory.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        isbn (str): The ISBN number of the book
        status (str): Current status - 'available' or 'issued'
    """
    
    def __init__(self, title, author, isbn, status="available"):
        """
        Initialize a Book object.
        
        Args:
            title (str): Book title
            author (str): Book author
            isbn (str): Book ISBN number
            status (str): Book status (default: 'available')
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status
    
    def __str__(self):
        """
        String representation of the Book object.
        
        Returns:
            str: Formatted string with book details
        """
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {self.status}"
    
    def __repr__(self):
        """
        Official string representation of the Book object.
        
        Returns:
            str: Representation string
        """
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', '{self.status}')"
    
    def to_dict(self):
        """
        Convert Book object to dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary representation of the book
        """
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'status': self.status
        }
    
    def issue(self):
        """
        Issue the book if available.
        
        Returns:
            bool: True if book was issued, False if already issued
        """
        if self.status == "available":
            self.status = "issued"
            return True
        return False
    
    def return_book(self):
        """
        Return the book if it was issued.
        
        Returns:
            bool: True if book was returned, False if already available
        """
        if self.status == "issued":
            self.status = "available"
            return True
        return False
    
    def is_available(self):
        """
        Check if the book is available.
        
        Returns:
            bool: True if available, False otherwise
        """
        return self.status == "available"
