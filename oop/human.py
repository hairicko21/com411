from inhabitant import Inhabitant
class Human(Inhabitant):
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Human" , age=0, energy=MAX_ENERGY):
    self.name = name
    self.age = age
    self.energy = energy
  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old. And my energy is{self.energy}'
  
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'


  def display(self):
   
    print(f"I am {self.name}, and my energy is, {self.energy}")


if (__name__ == "__main__"):
  # create an object of type Human
  human = Human()

  # display the current state of the object
  print(repr(human))

  # invoke the method move on the object
  human.move(10)
  human.eat(2)
  human.grow(4)
  human.grow(2)
  print(repr(human))
