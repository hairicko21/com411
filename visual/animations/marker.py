import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
data = None

def animate(frame):
  global data
  ax.cla()
  data = {
    'x':np.array([3, 3, 4, 4, 3]),
    'y':np.array([3, 4, 4, 3, 3])
  }
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 10)
  ax.plot(frame + data['x'], data['y'], 'r')
  # your code here

def run():
  global fig
  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  plt.show()
  # your code here

run()