print('What type of adventure should I have?')
response = input()

if ((response.lower() == 'scary') or (response.lower() == 'short')):
  print('Entering the dark forest!')

elif ((response.lower() == 'safe') or (response.lower() == 'long')):
  print('Taking the safe route!')

else:
  print('Not sure which route to take.')