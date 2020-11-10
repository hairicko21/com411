def directions():
  directions_list = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

  return directions_list

def run():
  directions()
  print('your directions are: {} '.format(directions()[1]))

run()