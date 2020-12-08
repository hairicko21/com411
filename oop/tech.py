from abc import ABC, abstractmethod

class Tech(ABC):
  #it has two abstract methods

  def __init__(self): # not necessary
    pass

  @abstractmethod
  def activate():
    pass
  
  @abstractmethod
  def deactivate():
    pass