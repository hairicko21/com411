print('what are you eating ? ')
response = input()

if (response.lower() == 'pizza' or (response.lower() == 'burger' or (response.lower() == 'tacos'))):
  print('you love fast food, i see and what you prefer to drink ?')
  drinks = input()

  if (drinks.lower() == 'Fanta') or (drinks.lower() == 'Coke'):
    print('you are a true heartbreaker')

  else:
    print('its nice')

elif (response.lower() == 'banana' or (response.lower() == 'apple' or (response.lower() == 'pineapple'))):
  if (response.lower() == 'banana'):
    print('Did you know bananas without B is Pineapple')
  elif (response.lower() == 'apple'):
    print('an apple a day keeps the doctor away')
  elif (response.lower() == 'pineapple'):
    print('Who lives in a pineapple under the sea ?')

else:
  print('im not sure what that is')