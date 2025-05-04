from LibraryManagementSystem.account import Account
from .models import *

class Librarian(Account):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    super().__init__(id, password, person, status)
  
  def add_book_item(self, book_item):
    None
  
  def block_member(self, member):
    None
  
  def un_block_member(self, member):
    None