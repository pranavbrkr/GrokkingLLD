from LibraryManagementSystem.search import Catalog


class Library:
  _instance = None

  def __init__(self):
    self._book_items = {}  # book_item_id -> BookItem
    self._lendings = {}    # book_item_id -> BookLending
    self._reservations = {}  # book_item_id -> BookReservations
    self._catalog = Catalog()
    self._notifications = []

  @classmethod
  def get_instance(cls):
    if cls._instance is None:
      cls._instance = Library()
    return cls._instance
  
  def get_catalog(self):
    return self._catalog

  def add_notification(self, notification):
    self._notifications.append(notification)
    notification.send_notification()

  def add_book_item(self, book_item):
    self._book_items[book_item.id] = book_item
    self._catalog.add_book(book_item)

  def add_lending(self, book_item_id, lending):
    self._lendings[book_item_id] = lending

  def get_lending(self, book_item_id):
    return self._lendings.get(book_item_id, None)

  def remove_lending(self, book_item_id):
    if book_item_id in self._lendings:
      del self._lendings[book_item_id]

  def add_reservation(self, reservation):
    self._reservations[reservation._item_id] = reservation

  def get_reservation(self, book_item_id):
    return self._reservations.get(book_item_id)

  def remove_reservation(self, book_item_id):
    if book_item_id in self._reservations:
      del self._reservations[book_item_id]