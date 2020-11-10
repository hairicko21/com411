def display_ladder(steps):
  print('|    |')

  for steps in range(steps):
    print('******')
    print('|    |')

def create_ladder():
  print('How many steps remain?')
  rem_steps = int(input())

  display_ladder(rem_steps)

create_ladder()
