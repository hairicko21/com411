#HUMAN class
class Human:
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Human" , age=0, energy=0):
    self.name = name
    self.age = age
    self.energy = energy
  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old. And my energy is{self.energy}'
  
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'
  
  def grow(self):
    self.age += 1
  
  def eat(self, amount):
    if (self.energy + amount > Human.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
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

  def display(self):
   
    print(f"I am {self.name}, and my energy is, {self.energy}")


if (__name__ == "__main__"):
  human = Human("Hayri", 19, 50)
  #human.grow()
  #human.move(0)
  #human.eat(20)
  #human.display()
  #print(str(human))
  print(repr(human))

#ROBOT class
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

#PLANET class
from human import Human
from robot import Robot
class Planet:
  def __init__(self):
    self.inhabitants = {'humans': [],'robots': []}
  def __str__(self):
    return f"planets(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']}"

  def __repr__(self):
    return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots ."    
    

  def add_human(self, human):
    self.inhabitants['humans'].append(Human)
  
  def remove_human(self, human):
    self.inhabitants['humans'].remove(Human)
  
  def add_robot(self, robot):
    self.inhabitants['robots'].append(Robot)

  def remove_robot(self, robot):
    self.inhabitants['robots'].remove(Robot)


  
  #def display(self):
    print(f"There is {self.humans} as part of human race, and {self.robots}, as part of robot race")

if (__name__ == "__main__"):
  planet = Planet()
  planet.__str__()
  planet.__repr__()
  planet.add_human('Hayri')
  planet.add_robot('Robocop')
  planet.add_robot('Beep')
  planet.add_robot('Bob')
  planet.add_robot('Prins')
  print(planet.__repr__())


# UNIVERSE class
import random
from planet import Planet
from robot import Robot
from human import Human
from inhabitant import Inhabitant
import matplotlib.pyplot as plt
class Universe:

  def __init__(self):
    self.planets = []

  def __repr__(self):
    return f"Universe(planets={self.planets})"

  def __str__(self):
    return f"The univers contains{len(self.planets)} planets."
  
  def generate(self):
    #generate new planet
    planet = Planet()


    for index in range(random.randint(1, 10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(robot)

    for index in range(random.randint(1, 10)):
      human = Human(f"Human{index}")
      planet.add_human(human)

    

    self.planets.append(planet)
  
  def show_populations(self):
    num_subplots = len(self.planets)
    
    fig = plt.figure()
    
    for index in range(num_subplots):
      planet = self.planets[index]
      num_humans = len(planet.inhabitants['humans'])
      num_robots = len(planet.inhabitants['robots'])

      ax = fig.add_subplot(1, num_subplots, index+1)
      ax.bar([1, 2], [num_humans, num_robots])
    

    plt.tight_layout()  
    plt.show()


# Should update that class with matplotlib.pyplot
if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.show_populations()