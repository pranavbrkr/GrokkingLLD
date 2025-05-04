from abc import ABC

class Book(ABC):
  def __init__(self, ISBN, title, subject, publisher, language, number_of_pages):
    self._ISBN = ISBN
    self._title = title
    self._subject = subject
    self._publisher = publisher
    self._language = language
    self._number_of_pages = number_of_pages
    self._authors = []
