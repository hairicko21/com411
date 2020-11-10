print('What level of brightness is required?')
lvl = int(input())
print()
print('Adjusting brightness...')

for count in range(0, lvl + 1, 2):
  print()
  print('Beep''s brightness level:', count * '*')
  print('Bop''s brightness level:', count * '*')
  print()

print('Adjustments complete!')