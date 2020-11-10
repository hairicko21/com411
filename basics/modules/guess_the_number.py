def play_guess_the_number():
  import random

  print('Please enter the minimum value:')
  minimum_value = int(input())

  print('Please enter the maximum value:')
  maximum_value = int(input())

  number = random.randrange(minimum_value, maximum_value)

  print("I am thinking of a number between {} and {}.  Can you guess what it is?".format(minimum_value, maximum_value))

  response = 0

  while (response != number):
    response = int(input())

    if (response == number):
      print('Congratulations! You guessed my number!')
      break
    elif (response < number):
      print('Your guess is too low.')
    
    elif (response > number):
      print('Your guess is too high.')

    else:
      print('Try again:')

def run():
  play_guess_the_number()
run()