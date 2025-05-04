class BookReservation:
  def __init__(self, creation_date, status, book_item_barcode, member_id):
    self._creation_date = creation_date
    self._status = status
    self._book_item_barcode = book_item_barcode
    self._member_id = member_id

  def fetch_reservation_details(self, barcode):
    None