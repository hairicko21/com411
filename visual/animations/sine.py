import matplotlib.pyplot as plt   
import matplotlib.animation as animation
import numpy as np
     
fig, ax = plt.subplots()
    
def animate(frame):
  ax.set_xlim(0, 720)
  ax.set_ylim(-1, 1)
  x = np.arange(0, frame)
  y_val = np.sin(x * (np.pi/180))
  ax.plot(x, y_val, 'ro')
  # your code here
     
def run():
  global fig 
  simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  plt.show()
  # your code here
      
run()  