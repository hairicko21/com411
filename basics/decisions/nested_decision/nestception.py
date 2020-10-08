print("Where should I look?")
response = input()

if (response.lower() == 'in the bedroom'):
  print('Where in the bedroom should I look?')

  response1 = input()

  if (response1.lower() == 'under the bed'):
    print('Found some shoes but no battery')
  
  else:
    print('Found some mess but no battery.')

elif(response.lower() == 'in the bathroom'):
  print('Where in the bathroom should I look?')

  response2 = input()

  if (response2.lower() == 'in the bathtub'):
    print('Found a rubber duck but no battery')

  else:
    print('Found a wet surface but no battery.')

elif(response.lower() == 'in the lab'):
  print('Where in the lab should I look?')

  response3 = input()

  if (response3.lower() == 'on the table'):
    print('Yes! I found my battery!')

  else:
    print('Found some tools but no battery.')

else:
  print('I do not know where that is but I will keep looking.')