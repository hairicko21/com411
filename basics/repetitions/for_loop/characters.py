print('What strange markings do you see?')
response = input()

print()
print('Identifying...')
print()


for marks in range(0, len(response), 1):
  print('index', marks + 1, ':', response[marks] )

print('Done!')
