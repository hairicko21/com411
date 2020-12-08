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
