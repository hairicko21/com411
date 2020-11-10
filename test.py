def gang():
    print("Loading gang...")
    
    friends = []
    friends.append("Scooby Doo")
    friends.append("Shaggy Rogers")
    friends.append("Fred Jones")
    friends.append("Daphne Blake")
    friends.append("Velma Dinkley")
    print(friends)
    print('...Done!')
    return friends

def phrases(friends):
    
    quotes = {}
    for friend in friends:
        print('What does {} say?'.format(friend))
        response = input()
        quote = response
        quotes['friend'] = quote
    return quotes

def save(quotes):
    with open(quotes.txt, 'w') as file:
        for item in quotes:
            file.write(f'{item[0]}: {quotes[1]}')

save(quotes) 
print("The file contains...")
file = open("quotes.txt")
print(file.read())
