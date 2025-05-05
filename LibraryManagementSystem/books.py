from abc import ABC, abstractmethod
from models import *

class Book(ABC):
  def __init__(self, isbn, title, subject, publisher, language, number_of_pages, book_format):
    self._isbn = isbn
    self._title = title
    self._subject = subject
    self._publisher = publisher
    self._language = language
    self._number_of_pages = number_of_pages
    self._book_format = book_format
    self._authors = []

class BookItem(Book):
  def __init__(self, id, book, is_reference_only, borrowed, due_date, price, status, date_of_purchase, publication_date, placed_at):
    super().__init__(None, None, None, None, None, 0, None)  # Calling the parent class constructor
    self.id = id
    self.book = book
    self.is_reference_only = is_reference_only
    self.borrowed = borrowed
    self.due_date = due_date
    self.price = price
    self.status = status
    self.date_of_purchase = date_of_purchase
    self.publication_date = publication_date
    self.placed_at = placed_at
  
  def checkout(self, member_id):
    return True
  
  def set_placed_at(self, rack):
    self.placed_at = rack
  
  def set_added_by(self, librarian):
    pass

  def get_book(self):
    return self.book

  def is_available(self):
      return self.status == BookStatus.AVAILABLE and not self.is_reference_only


class Rack:
  def __init__(self, number, location_identifier):
    self._number = number
    self._location_identifier = location_identifier
    self._book_items = []
  
  def add_book_item(self, book_item):
    self._book_items.append(book_item)