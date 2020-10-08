print('Towards which direction should I paint (up, down, left or right)?')

response = input()

if (response.lower() == 'up'):
  print('I am painting in the upward direction!')

elif (response.lower() == 'down'):
  print('I am painting in the downwards direction!')

elif (response.lower() == 'left'):
  print('I am painting in the left direction!')

elif (response.lower() == 'right'):
  print('I am painting in the right direction!')

else:
  print('i am not sure which direction to go')