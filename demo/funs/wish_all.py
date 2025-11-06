def wish(*names,  message ):
    for n in names:
        print(message, n)


wish('Andy', 'Bill', 'Clark', message = 'Hi')
wish('Mark', 'Jack', message = 'Hello')
