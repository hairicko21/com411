import matplotlib.pyplot as plt



def read_data(file_path):
  temps = []
  file = open(file_path)
  lines = file.readlines()

  for line in lines:
    temps.append(line.strip())
  file.close()
  
  return temps

def run():
  data = read_data('visual/subplots/temps.txt')

  fig, axes = plt.subplots(2,2, sharex='all')

  x = range(0, 7, 1)
  y = data

  plt.xlabel('day')
  plt.ylabel('Temperature')

  axes[0, 0].plot(x, y)
  axes[0, 1].bar(x, y)

  plt.tight_layout()
  plt.show()

run()
