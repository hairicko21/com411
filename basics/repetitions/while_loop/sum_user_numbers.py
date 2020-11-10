print('How many numbers should I sum up?')
numbers = int(input())
summed = 0

print()

total = 0

while (summed < numbers):
 print("Please enter number", summed, "of", numbers, ":")

 numbers1 = int(input())
 total = total + numbers1
 summed = summed + 1

print("The answer is", total)


