# User is an abstract class
from abc import ABC, abstractmethod

class Notification(ABC):
  def __init__(self, notification_id, creation_date, content, user):
    self._notification_id = notification_id
    self._creation_date = creation_date
    self._content = content
    self._user = user
    # self._book_lending = None
    # self._book_reservation = None

  @abstractmethod
  def send_notification(self):
    pass

class PostalNotification(Notification):
  def __init__(self, notification_id, creation_date, content, user, address):
    super().__init__(notification_id, creation_date, content, user)
    self._address = address
  
  def send_notification(self):
      print(f"[POSTAL] To: {self._address._street_address}\n{self._content}") 

class EmailNotification(Notification):
  def __init__(self, notification_id, creation_date, content, user, email):
    super().__init__(notification_id, creation_date, content, user)
    self._email = email

  def send_notification(self):
      print(f"[EMAIL] To: {self._email}\n{self._content}")