def observed():
  observations = []

  for count in range(7):
    print('Please enter an observation:')
    answer = input()

    observations.append(answer)
  
  return observations

def run():
  print("Counting observations...")

  observasions = observed()

  observasion_set = set()

  for observasion in observasions:
    occurences = observasions.count(observasion)
    observasion_set.add( (observasion, occurences) )

  for key, value in observasion_set:
    print(f'{key} observed {value} ''times')

  print(observasion_set)
   


run()

