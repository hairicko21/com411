import matplotlib.pyplot as plt
import random as rnd
def data():
  paths = {}

  print('What type of line would you like?(:,--,-) ')
  type_line = input()

  print('What colour would you like ?(r,g,b) ')
  colour_line = input()

  print('What style of marker would you like ?(o,s,^) ')
  marker_line = input()

  paths['type_line'] = type_line
  paths['colour_line'] = colour_line
  paths['marker_line'] = marker_line

  return paths

def generate():
  print('How many lines would you like to display?')
  lines = int(input())
  for line in range(lines):
    datas = data()
    x = [1,rnd.randrange(1,10)]
    y = [1,rnd.randrange(1,10)]

    plt.plot(x, y, f"{datas['type_line']}{datas['colour_line']}{datas['marker_line']}")

  plt.show()

def run():
  print('Running...')
  generate()
  print('Done !')

run()