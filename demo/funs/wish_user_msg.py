def wish(user, message):
    print(message, user)

# Pass by position
wish('Kevin', 'Hi')
wish('Andy', 'Hello')

# Pass by keyword args
wish(message = 'Hi', user = 'Micheal')
