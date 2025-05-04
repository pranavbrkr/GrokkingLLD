from LibraryManagementSystem.account import Account
from LibraryManagementSystem.book_reservation import BookReservation
from .models import *
from datetime import datetime
from .constants import *

class Member(Account):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    super().__init__(id, password, person, status)
    self._date_of_membership = datetime.date.today()
    self._total_books_checkedout = 0
  
  def get_total_books_checkedout(self):
    return self._total_books_checkedout
  
  def reserve_book_item(self, book_item):
    None
  
  def increment_total_books_checkedout(self):
    None
  
  def renew_book_item(self, book_item):
    None
  
  def checkout_book_item(self, book_item):
    if self.get_total_books_checkedout() >= Constants.MAX_BOOKS_ISSUED_TO_A_USER:
      print("The user has already checked out maximum number of books")
      return False
    book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())
    