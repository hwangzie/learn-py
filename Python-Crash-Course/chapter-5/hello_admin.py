usernames = ['admin', 'john', 'jane', 'doe', 'joe']

for nick in usernames:
    if nick == 'admin':
        print(f'Hello {nick}, would you like to see a status report?')
    else:
        print(f'Hello {nick}, thank you for logging in again.')

usernames = []

if len(usernames) == 0:
        print('We need to find some users!')
else:
     for nick in usernames:
        if nick == 'admin':
            print(f'Hello {nick}, would you like to see a status report?')
        else:
            print(f'Hello {nick}, thank you for logging in again.')
    


    