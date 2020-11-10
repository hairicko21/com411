print('Program Started!')
print()
print('Please enter an ASCII code:')

code = int(input())
lowest = 32
highest = 126

if code in range(lowest, highest):
  letter = chr(code)
  print("The character represented by the ASCII code {} is {}.".format(code, letter))

elif code not in range(lowest, highest):
  print('The code is not correct')

print("Program Ended!", end="")