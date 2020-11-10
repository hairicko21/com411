print('What phrase do you see?')
response = input()
print()
print('Reversing...')
print()
print('The phrase is ', end="")
for reverse in range(len(response) - 1, -1, -1):
 
  print(response[reverse], end="")