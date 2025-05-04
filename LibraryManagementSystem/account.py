from abc import ABC
from datetime import datetime
from .models import *

class Account(ABC):
  def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
    self._id = id
    self._password = password
    self._status = status
    self._person = person
  
  def reset_password(self):
    None