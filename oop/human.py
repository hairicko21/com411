class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  # An instance method
  def display(self):
    print(f"I am {self.name}")


if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  Robot.the_laws()
  print(repr(robot))

class Human:
  MAX_ENERGY = 100

  #initialiser
  def __init__(self):
    self.name = 'Human'
    self.age = 0
    self.energy = Human.MAX_ENERGY
  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old.'

  def display(self):
   
    print(f"I am {self.name}")


if (__name__ == "__main__"):
  human = Human()
  human.display()
  print(str(human))
