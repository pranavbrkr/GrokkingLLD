class Fine:
  def __init__(self, creation_date, book_item_barcode, member_id):
    self._creation_date = creation_date
    self._book_item_barcode = book_item_barcode
    self._member_id = member_id
  
  def collect_fine(self, member_id, days):
    None