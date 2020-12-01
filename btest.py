import matplotlib.pyplot as plt 



def data():
  triangles = {}
  x = [3, 5, 7, 3]
  y = [3, 5, 3, 3]
  triangle1 = ('x'=[3, 5, 7, 3], 'y'= [3, 5, 3, 3])

  axes[0, 0].plot(x, y, 'ro--')
  
  x1 = [3, 5, 7, 3]
  y1 = [5, 3, 5, 5]

  axes[0, 1].plot(x1, y1, 'sb:')
  
  x2 = [3, 3, 7, 3]
  y2 = [3, 5, 4, 3]
  axes[1, 0].plot(x2, y2, 'g*-.')

  x3 = [7, 7, 3, 7]
  y3 = [3, 5, 4, 3]
  axes[1, 1].plot(x3, y3, 'yp-')



  

def improved_separated():
