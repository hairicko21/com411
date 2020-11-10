print('How many rows should I have?')
rows = int(input())

print('How many columns should I have?')
columns = int(input())

print()
print('Here i go:')

for count in range(0, rows, 1):
    for number in range(0, columns, 1):
         print(number * ':-)', end="")
    print()
print()

print('Done!')