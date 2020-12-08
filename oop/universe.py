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
      planet.add(robot)

    for index in range(random.randint(1, 10)):
      human = Human(f"Human{index}")
      planet.add(human)

    

    self.planets.append(planet)
  
  def show_populations(self):
    num_subplots = len(self.planets)
    
    fig = plt.figure()
    
    for index in range(num_subplots):
      planet = self.planets[index]
      
      num_humans = 0
      num_robots = 0

      for inhabitant in planet.inhabitants:
        if isinstance(inhabitant, Human):
          num_humans += 1
        elif isinstance(inhabitant, Robot):
          num_robots += 1 

      ax = fig.add_subplot(1, num_subplots, index+1)
      ax.bar([1, 2], [num_humans, num_robots])
    
    plt.tight_layout()
    plt.show()
   


# Should update that class with matplotlib.pyplot
if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.show_populations()