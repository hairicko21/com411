print('how many cables should i avoid ?')
response = int(input())

live_cables = 0

while (live_cables < response):

  live_cables = live_cables + 1

  print('avoiding...Done!', live_cables, ' live cable avoided!') 

print('All live cables have been avoided.', end="")