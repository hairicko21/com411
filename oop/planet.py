from human import Human
from robot import Robot
from inhabitant import Inhabitant
class Planet:
  def __init__(self):
    self.inhabitants = []

  def __str__(self):
    self.num_humans = 0
    self.num_robots = 0
    for inhabitant in planet.inhabitants:
      if isinstance(inhabitant, Human):
        self.num_humans += 1
      elif isinstance(inhabitant, Robot):
        self.num_robots += 1
    return f"planets(humans={self.num_humans}, robots={self.num_robots}"



  def __repr__(self):
    return f"This planet has {self.num_humans} humans and {self.num_robots} robots ."    
    

  def add(self, inhabitant):
    self.inhabitants.append(inhabitant)
  
  def remove(self, inhabitant):
    self.inhabitants.remove(inhabitant)
  


  
  #def display(self):
    print(f"There is {self.inhabitants} as part of human race, and {self.inhabitants}, as part of robot race")

if (__name__ == "__main__"):
  planet = Planet()
  hayri  = Human('Hayri')
  Go6ko = Robot("Go6ko")
  planet.add_inhabitant(hayri)
  planet.add_inhabitant(Go6ko)
  print(str(planet))
  planet.__repr__()
  print(planet.__repr__())