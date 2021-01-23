users = ['admin', 'tal', 'ofri', 'yahel', 'sky']
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to ban everyone ?')
        else:    
            print(f'Hello {user.title()}, happy to see you again!')
else:
    print("We need to find some users")