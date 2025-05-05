from models import ReservationStatus

class BookReservations:
  def __init__(self, creation_date, item_id, member_id):
      self._creation_date = creation_date
      self._status = ReservationStatus.WAITING
      self._item_id = item_id
      self._member_id = member_id

  
  def fetch_reservation_details(self, book_item_id):
    return self._item_id, self._member_id, self._status

class BookLending:
  def __init__(self, creation_date, due_date, book_item_id, member_id):
    self._creation_date = creation_date
    self._due_date = due_date
    self._return_date = None
    self._book_item_id = book_item_id
    self._member_id = member_id
    self._book_reservation = None
    self._user = None
  
  def lend_book(self, item_id, member_id):
    None

  def fetch_lending_details(self, item_id):
    None


class Fine:
  def __init__(self, creation_date, book_item_id, member_id, amount):
    self._creation_date = creation_date
    self._book_item_id = book_item_id
    self._member_id = member_id
    self._amount = amount
    self._paid = False

  def collect_fine(self):
    self._paid = True
    print(f"Fine of ${self._amount} collected from member {self._member_id}")