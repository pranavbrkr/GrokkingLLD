class BookReservations:
  def __init(self, creation_date, status, item_id, member_id):
    self._creation_date = creation_date
    self._status = status
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
  def __init__(self, creation_date, book_item_id, member_id):
    self._creation_date = creation_date
    self._book_item_id = book_item_id
    self.member_id = member_id

  def collect_fine(self, member_id, days):
    None