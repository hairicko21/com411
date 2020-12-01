import matplotlib.pyplot as plt 

def combined():
  x = [3, 5, 7, 3]
  y = [3, 5, 3, 3]

  plt.plot(x, y, 'ro--')
  
  x1 = [3, 5, 7, 3]
  y1 = [5, 3, 5, 5]

  plt.plot(x1, y1, 'sb:')
  
  x2 = [3, 3, 7, 3]
  y2 = [3, 5, 4, 3]
  plt.plot(x2, y2, 'g*-.')

  x3 = [7, 7, 3, 7]
  y3 = [3, 5, 4, 3]
  plt.plot(x3, y3, 'yp-')
  plt.show()

def separated()

combined()