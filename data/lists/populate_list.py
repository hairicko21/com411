def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

  return directions

def menu():
  print('Please select a direction:')
  
  direction = directions()

  for index in range(len(direction)):
    print('{}: {}'.format(index, direction[index]))

  pick = int(input())


  return direction[pick]

def run():
  route = []

  print("Working out escape route...")
  
  
  for count in range(5):
   direction = menu()
   route.append(direction)
  
  print('Escape route: {}'.format(route))
    
    
run()