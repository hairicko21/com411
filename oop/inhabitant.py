class Inhabitant:

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
    self.name = name
    self.age = age
    self.energy = energy
  
  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
      self.energy = potential_energy
      return 0
    return distance
  
  def eat(self, amount):
    if (self.energy + amount > Inhabitant.MAX_ENERGY):
      self.energy = Inhabitant.MAX_ENERGY
    else:
      self.energy += amount
  
  def grow(self, years=1):
    self.age += years
