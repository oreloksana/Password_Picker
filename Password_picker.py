import random
import string

while True:
    adjectives = ['slipy', 'sla0w', 'smally',
    'weeett', 'fet', 'red',
    '0rang', 'yellow', 'green',
    'blÜ', 'purpl', 'flufy',
    'white', 'prud', 'brev']

    nouns = ['eple', 'dinoswr', 'bol',
    'toster', 'got', 'dregon',
    'hamer', 'dak', 'penda']

    colours = ["rEd", "Bl0u", "GreeN", "Bl@ck", "wh!te", "yell0w", "turkis"]

    print('Welcome to Password Picker!')

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    colour = random.choice(colours)

    number = random.randrange(0, 100)

    special_char = random.choice(string.punctuation)

    password = adjective + noun + special_char + colour + str(number) + special_char
    print('Your new password is: %s' % password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break