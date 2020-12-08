class Robot:
  MAX_ENERGY = 100

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name = "Robot", age=0, energy=0):

    # An instance attribute
    self.name = name
    self.age = age
    self.energy = energy
 
 #magic methods
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old. And my energy is {self.energy}'
  
  #instance methods
  def grow(self):
    self.age += 1

  def eat(self, amount):
    if (self.energy + amount > Robot.MAX_ENERGY):
      self.energy = Robot.MAX_ENERGY
    else:
      self.energy += amount

    return amount
  
  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
      self.energy = potential_energy
      return 0
    return distance


  # An instance method
  def display(self):
    print(f"I am {self.name}, and i have energy of {self.energy}")


if (__name__ == "__main__"):
  robot = Robot("Beep", 3, 60)
  robot.eat(45)
  robot.move(34)
  robot.display()
  Robot.the_laws()
  print(repr(robot))