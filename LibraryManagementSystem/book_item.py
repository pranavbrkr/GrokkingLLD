from LibraryManagementSystem.book import Book
from LibraryManagementSystem.book_lending import BookLending
from .models import *


class BookItem(Book):
  def __init__(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status, date_of_purchase, publication_date, placed_at):
    self._barcode = barcode
    self._is_referenced_only = is_reference_only
    self._borrowed = borrowed
    self._due_date = due_date
    self._price = price
    self._format = book_format
    self._status = status
    self._date_of_purchase = date_of_purchase
    self._publication_date = publication_date
    self._placed_at = placed_at
  
  def checkout(self, member_id):
    if self.get_is_reference_only():
      print("self book is reference only and can't be issued")
      return False
    if not BookLending.lend_book(self.get_bar_code(), member_id):
      return False
    self.update_book_item_status(BookStatus.LOANED)
    return True