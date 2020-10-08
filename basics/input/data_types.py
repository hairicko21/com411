#ask user to enter their name
print('What is your name human?')
user_name = input()
print()
#ask user to tell his age
print('How old are you (in years)?')
user_age = int(input())
print()
#ask user to tell his heigh
print('How tall are you (in meters)?')
user_heigh = float(input())
print()
#ask user to tell his weigh
print('How much do you weigh (in kilograms)?')
user_weigh = float(input())
print()
#calculate
bmi = user_weigh / (user_heigh ** 2)
#display
print('Your name is ', str(user_name), ' and your bmi is ',bmi)