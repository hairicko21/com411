def climb_ladder(rem_steps, crossed_steps):
  if rem_steps > crossed_steps:
    print('Still some way to go!')
  
  elif rem_steps < crossed_steps:
    print('We are almost there!')


climb_ladder(5, 2)
climb_ladder(2, 5)