names = ['toto', 'admin', 'guess', 'tulits', 'jason', 'oniks', 'samantha']
names.append('railey')

ban_user = ['tulits', 'oniks' ]
ban_user.append('jason')

login = input('\nPls login your name: ').lower() #all inputs will be in lowercase
#for BAN USER


if login in ban_user:
    print(login + ' You are not allowed to enter')
elif login in names:
    print(login + ' Welcom to METAVERSE!!')
else:
    print(login + ' Account doesnt exist.Create now?')
