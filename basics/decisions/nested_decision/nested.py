print ('What type of cover does the book have(hard or soft)?')
cover = input()

if (cover.lower() == 'soft'):
  print('Is the book perfect-bound?(yes or no)')
  perfect_bound = input()

  if (perfect_bound.lower() == 'yes'):
    print('Soft cover, perfect bound books are very popular!')

  elif (perfect_bound.lower() == 'no'):
    print('Soft covers with coils or stitches are great for short books')
  
  else:
    print('i dont thik that answers my question')

if (cover.lower() == 'hard'):
  print('Books with hard covers can be more expensive!')