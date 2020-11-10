print('Program Started!')
print()
print('Please enter a standard character:')

standard_character = input()

if (len(standard_character) == 1):
 
  print('The ASCII code for: {}'.format(standard_character), ' is {}'.format(ord(standard_character)))

elif not (len(standard_character) == 1):
  print('Error, not a standart character')

print()

print('Program Ended!', end="")