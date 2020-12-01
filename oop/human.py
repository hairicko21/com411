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
  
  def grow(self):
    self.age += 1

  def eat(self, amount):
    self.energy += amount

    return amount
  
  def move(self, distance):
    self.energy -= distance

    return distance


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
  def __init__(self, name, age, energy):
    self.name = name
    self.age = age
    self.energy = energy
  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old.'
  
  def grow(self):
    self.age += 1
  
  def eat(self, amount):
    self.energy += amount

    return amount
  
  def move(self, distance):
    self.energy -= distance

    return distance

  def display(self):
   
    print(f"I am {self.name}, and my energy is, {self.energy}")


if (__name__ == "__main__"):
  human = Human("Hayri", 19, 50)
  human.grow()
  human.move(0)
  human.eat(20)
  human.display()
  print(str(human))
