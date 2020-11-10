def likelihood():
  likelihood = (50, 38, 27, 99, 4)
  return min(likelihood), max(likelihood)
  

def run():
  likelihoods = likelihood()
  print("Minimum likelihood of falling: {}%".format(likelihoods[0]))
  print('Maximum likelihood of falling: {}%'.format(likelihoods[1]))

run()