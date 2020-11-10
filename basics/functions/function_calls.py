def display_box():
  print('what the word shloud be ?')
  word = input()
  num = len(word) + 8
  print('-' * num)
  print('|   {}   |'.format(word))
  print('-' * num)

def display_lowercase():
  print('what the word shloud be ?')
  word = input()
  print(word.lower())

def display_uppercase():
  print('what the word shloud be ?')
  word = input()
  print(word.upper())

def display_mirror():
  print('what the word shloud be ?')
  word = input()
  reverse_word = ''

  for letter in reversed(word):
        reverse_word += letter

  print("{} | {}".format(word, reverse_word))

def Repeat():
  print('what the word shloud be ?')
  word = input()
  print('how many times to repeat the word ?')
  repeat = int(input())

  for repetition in range(repeat):
    if repetition % 2 == 0:
      print(word.lower())
    else:
      print(word.upper())

def run():
  display_box()
  display_lowercase()
  display_uppercase()
  display_mirror()
  Repeat()

run()
  
