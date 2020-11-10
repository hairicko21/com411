print('How many bars should be charged?')
response = int(input())

Charged_cables = 1

while (Charged_cables <= response):

  print('Charged:', '█ ' * Charged_cables)

  Charged_cables = Charged_cables + 1

print('The battery is fully charged.', end="")