import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 10)
  ax.plot(frame, frame, 'ro')
  # your code here

def run():
  global fig
  simple_animation=animation.FuncAnimation(fig,animate,frames=10,interval=100)
  plt.show()
  # your code here

run()