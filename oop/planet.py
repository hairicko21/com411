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
  
