

def search(filename):
  print("Searching...")


  with open(filename) as file:
    for line in file:
      print(f'Looked in: {line}', end='')

  print('Done!')

def run():
  search("data/files/txt/locations.txt")

run()