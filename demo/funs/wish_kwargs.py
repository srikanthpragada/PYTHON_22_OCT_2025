# Keyword-only args
def wish(*, message, name):
    print(message, name)


#wish('Scott', 'Hi')
wish(message = 'Hi', name  = 'Scott')
