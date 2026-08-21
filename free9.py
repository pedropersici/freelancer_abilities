enter = input('Do you want to [E]nter or [F]inish? : ').upper()
if enter == 'E':
    password = input('Enter your password: ')
    permited_password = ['123456']

    if enter == 'E' and password == permited_password:
        print('Access granted!')
    else:
        print('Access denied!')
