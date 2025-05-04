from LibraryManagementSystem.search import Search

class Catalog(Search):
  def __init__(self):
    self._book_titles = {}
    self._book_authors = {}
    self._book_subjects = {}
    self._book_publication_dates = {}

  def search_by_title(self, query):
    return self._book_titles.get(query)

  def search_by_author(self, query):
    return self._book_authors.get(query)