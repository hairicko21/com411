print('How far are we from the cave?')
distance = int(input())

for count in range(0, distance, 1):
  
  print(distance, 'steps remaining')
  distance -= 1
print()

print('We have reached the cave!', end="")