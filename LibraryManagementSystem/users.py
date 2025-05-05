from abc import ABC, abstractmethod
import datetime

from book_transactions import BookLending, BookReservations
from library import Library
from notification import EmailNotification, PostalNotification
from models import *
from constants import *

class User(ABC):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    self._id= id
    self._passowrd = password
    self._status = status
    self._person = person
  
  @abstractmethod
  def reset_password(self):
    pass

class Librarian(User):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    super().__init__(id, password, person, status)

  def add_book_item(self, book_item):
    book_item.set_added_by(self)
    pass

  def block_member(self, member):
    None
  
  def unblock_member(self, member):
    None
  
  def reset_password(self):
    pass

class Member(User):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    super().__init__(id, password, person, status)
    self._date_of_membership = datetime.date.today()
    self._total_books_checked_out = 0
    self.card = LibraryCard(card_number=f"LIB-{id}", issued_date=datetime.date.today())
  
  def reserve_book_item(self, book_item):
    library = Library.get_instance()
    existing = library.get_reservation(book_item.id)

    if existing:
        print(f"Book {book_item.id} already reserved by another member.")
        return False

    reservation = BookReservations(
        creation_date=datetime.date.today(),
        item_id=book_item.id,
        member_id=self._id
    )
    library.add_reservation(reservation)
    book_item.status = BookStatus.RESERVED

    print(f"Book {book_item.id} reserved by member {self._id}")
    return True
  
  def increment_total_books_checked_out(self):
    None
  
  def checkout_book_item(self, book_item):
    if book_item.is_reference_only:
      print("Cannot checkout a referencce only book")
      return False

    if book_item.status != BookStatus.AVAILABLE:
      print("Book is not available for checkout")
      return False
    
    if self._total_books_checked_out >= MAX_BOOKS_ISSUED_TO_A_USER:
      print("User has reached maximum allowed checkouts")
      return False
    
    library = Library.get_instance()
    reservation = library.get_reservation(book_item.id)
    if reservation and reservation._member_id != self._id:
      print("Book is reserved by another member.")
      return False
    elif reservation and reservation._member_id == self._id:
      library.remove_reservation(book_item.id)

    lending = BookLending(
      creation_date = datetime.date.today(),
      due_date = datetime.date.today() + datetime.timedelta(days = DEFAULT_LENDING_DAYS),
      book_item_id = book_item.id,
      member_id = self._id
    )

    book_item.status = BookStatus.LOANED
    book_item.borrowed = True
    book_item.due_date = lending._due_date
    self._total_books_checked_out += 1
    library.add_lending(book_item.id, lending)

    notification = EmailNotification(
      notification_id=f"N-{book_item.id}",
      creation_date=datetime.date.today(),
      content=f"You checked out '{book_item.get_book()._title}'. Due on {book_item.due_date}",
      user=self,
      email=self._person._email
    )
    library.add_notification(notification)

    print(f"Book {book_item.id} successfully checked out by member {self._id}")
    return True
  
  def check_for_fine(self, book_item_id):
    library = Library.get_instance()
    lending = library.get_lending(book_item_id)

    if not lending:
        print("No lending found.")
        return 0

    today = datetime.date.today()
    due_date = lending._due_date

    if today > due_date:
        days_late = (today - due_date).days
        fine_amount = days_late * 1  # $1 per day
        print(f"Book is {days_late} days late. Fine: ${fine_amount}")

        notification = PostalNotification(
            notification_id=f"FINE-{book_item_id}",
            creation_date=today,
            content=f"Your book '{book_item_id}' is {days_late} days overdue. Fine: ${fine_amount}",
            user=self,
            address=self._person._address
        )
        library.add_notification(notification)
        return fine_amount
    else:
        print("No fine.")
        return 0

  def return_book_item(self, book_item):
    library = Library.get_instance()
    lending = library.get_lending(book_item.id)

    if not lending:
        print("No lending record found for this book.")
        return False

    reservation = library.get_reservation(book_item.id)
    if reservation:
        book_item.status = BookStatus.RESERVED
        print(f"Book {book_item.id} reserved by member {reservation._member_id}, not made available.")
    else:
        book_item.status = BookStatus.AVAILABLE

    book_item.borrowed = False
    book_item.due_date = None
    lending._return_date = datetime.date.today()
    library.remove_lending(book_item.id)
    self._total_books_checked_out -= 1

    notification = EmailNotification(
        notification_id=f"RETURN-{book_item.id}",
        creation_date=datetime.date.today(),
        content=f"You returned '{book_item.get_book()._title}' on {lending._return_date}.",
        user=self,
        email=self._person._email
    )
    library.add_notification(notification)

    print(f"Book {book_item.id} returned by member {self._id}")
    return True


  def renew_book_item(self, book_item):
    None
  
  def reset_password(self):
    pass

class LibraryCard:
    def __init__(self, card_number, issued_date):
        self.card_number = card_number
        self.issued_date = issued_date
        self.active = True

    def is_active(self):
        return self.active