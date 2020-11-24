import matplotlib.pyplot as plt   
import matplotlib.animation as animation
import numpy as np
     
fig, ax = plt.subplots()
    
def animate(frame): 
  ax.cla()
  ax.set_xlim(0, np.pi)
  ax.set_ylim(-1, 1)
  x_val = np.arange(0, 2*np.pi)
  y_val = np.sin(x_val + frame / 50)

  ax.plot(x_val, y_val, 'r')   
  # your code here
     
def run():
  global fig
  some_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 10) 
  plt.show() 
  # your code here
      
run()  