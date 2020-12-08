from tech import Tech


class Laser(Tech):

  MAX_RANGE = 100

  def __init__(self):
    super().__init__()

  def __repr__(self):
    return f"Laser()"
  def activate():
    print("Laser has been activated.")
  


  def deactivate():
    print("Laser has been deactivated.")

  def fire(range_dist):
    if (range_dist > Laser.MAX_RANGE):
      print(f"Fire maximum range of {Laser.MAX_RANGE}")

    else:
      print(f"Fired a distance of {range_dist}")  







if __name__ == "__main__":
  laser = Laser()