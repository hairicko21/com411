def observed():
  observations = []

  for count in range(5):
    print('Please enter an observation:')
    answer = input()
    observations.append(answer)

  return observations

def remove_observations(observations):
  is_running = True

  while(is_running):
    print('Do you wish to remove an observation (yes/no)?')
    answer = input()

    if (answer == 'yes'):
      print('What observation do you wish to remove?')
      to_remove = input()
      observations.remove(to_remove)
    else:
      is_running = False

def run():
  observations = observed()
  remove_observations(observations)
  observations_set = set()
  for observation in observations:
    occurrences = observations.count(observation)
    observations_set.add( (observation, occurrences) )

  for key, value in sorted(observations_set):
    print(f'{key} observed {value} times')

run()