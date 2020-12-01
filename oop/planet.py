class Planet:
  def __init__(self):
    self.humans = []
    self.robots = []

  def add_human(self, human):
    self.humans.append(human)
  
  def remove_human(self, human):
    self.humans.remove(human)
  
  def add_robot(self, robot):
    self.robots.append(robot)

  def remove_robot(self, robot):
    self.robots.remove(robot)

  def __str__(self):
    return self.humans, self.robots

  def __repr__(self):
    return self.humans, self.robots
  

if (__name__ == "__main__"):
  planet = Planet()
  planet.__str__()
  planet.__repr__()
  planet.add_human('person1')

  print(planet.__repr__())
