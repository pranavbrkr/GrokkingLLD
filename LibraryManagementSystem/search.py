from abc import ABC, abstractmethod

class Search(ABC):
  def search_by_title(self, title):
    None

  def search_by_author(self, author):
    None

  def search_by_subject(self, subject):
    None

  def search_by_publication_date(self, publish_date):
    None


class Catalog(Search):
  def __init__(self):
    self._book_titles = {}
    self._book_authors = {}
    self._book_subjects = {}
    self._book_publication_dates = {}

  def search_by_title(self, title):
    return list(self._book_titles.get(title, []))

  def search_by_author(self, author):
    return list(self._book_authors.get(author, []))

  def search_by_subject(self, subject):
    return list(self._book_subjects.get(subject, []))

  def search_by_publication_date(self, publish_date):
    return list(self._book_publication_dates.get(publish_date, []))
  
  def add_book(self, book_item):
    book = book_item.get_book()

    if not book:
      return

    self._book_titles.setdefault(book._title, set()).add(book_item)

    for author in book._authors:
      self._book_authors.setdefault(author, set()).add(book_item)
    
    self._book_subjects.setdefault(book._subject, set()).add(book_item)

    self._book_publication_dates.setdefault(book._publisher, set()).add(book_item)