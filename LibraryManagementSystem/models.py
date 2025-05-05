from abc import ABC
from enum import Enum

class BookFormat(Enum):
  HARDCOVER = 1
  PAPERBACK = 2
  AUDIO_BOOK = 3
  EBOOK = 4
  NEWSPAPER = 5
  MAGAZINE = 6
  JOURNAL = 7

class BookStatus(Enum):
  AVAILABLE = 1
  RESERVED = 2
  LOANED = 3
  LOST = 4

class ReservationStatus(Enum):
  WAITING = 1
  PENDING = 2
  CANCELLED = 3
  NONE = 4

class AccountStatus(Enum):
  ACTIVE = 1
  CLOSED = 2
  CANCELLED = 3
  BLACKLISTED = 4
  NONE = 5

class Address:
  def __init__(self, street, city, state, zip_code, country):
    self._street_address = street
    self._city = city
    self._state = state
    self._zip_code = zip_code
    self._country = country

class Person(ABC):
  def __init__(self, name, address, email, phone):
    self._name = name
    self._address = address
    self._email = email
    self._phone = phone