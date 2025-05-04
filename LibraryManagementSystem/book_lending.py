class BookLending:
  def __init__(self, creation_date, due_date, book_item_barcode, member_id):
    self._creation_date = creation_date
    self._due_date = due_date
    self._return_date = None
    self._book_item_barcode = book_item_barcode
    self._member_id = member_id
  
  def lend_book(self, barcode, member_id):
    None
  
  def fetch_lending_details(self, barcode):
    None