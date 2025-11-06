# postional-only args
def wish(name, message, /):
    print(message, name)


wish('Scott', 'Hi')
#wish(message = 'Hi', name  = 'Scott')
