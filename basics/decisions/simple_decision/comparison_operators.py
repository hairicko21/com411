print('Please enter the first number')
first = int(input())
print('Please enter the second number')
second = int(input())

if (first < second):
  print('{} is smaller than {}'.format(first, second))
elif (first > second):
  print('{} is bigger than {}'.format(first, second))
elif (first == second):
  print('{} is equal to {}'.format(first, second))