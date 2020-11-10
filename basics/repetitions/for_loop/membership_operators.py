print('What phrase do you see?')
response = input()

print('Reversing...')
print()
print('The phrase is:', end="")

reversed = ""

for letter in response:
  reversed = letter + reversed

print((reversed), end="")