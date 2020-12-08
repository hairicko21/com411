from inhabitant import Inhabitant
class Robot(Inhabitant):
  MAX_ENERGY = 100

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name = "Robot", age=0, energy=MAX_ENERGY):

    # An instance attribute
    self.name = name
    self.age = age
    self.energy = energy
 
 #magic methods
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old. And my energy is {self.energy}'

  # An instance method
  def display(self):
    print(f"I am {self.name}, and i have energy of {self.energy}")


if (__name__ == "__main__"):
  # create an object of type Human
  robot = Robot()

  # display the current state of the object
  print(repr(robot))

  # invoke the method move on the object
  robot.move(10)