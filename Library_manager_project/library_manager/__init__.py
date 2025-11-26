"""
Library Inventory Manager Package
A simple library management system for tracking books.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .book import Book
from .inventory import LibraryInventory

__all__ = ['Book', 'LibraryInventory']
