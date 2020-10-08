print('Please enter a whole number.')
response = int(input())

if (response % 2 == 0):
  print('{} is even'.format(response))
else:
  print('{} is odd'.format(response))