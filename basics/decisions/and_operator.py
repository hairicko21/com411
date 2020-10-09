print('What did I hear?')
response = input()
print (response)

print('What did I see?')
response1 = input()
print (response1)

if ((response.lower() == 'grrr') and (response1.lower() == 'two red eyes')):
  print('There is a scary creature. I should get out of here!')

else:
  print('I am a little scared but I will continue.')