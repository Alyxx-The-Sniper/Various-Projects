#
#
#
#
names = ['toto', 'admin', 'guess', 'tulits', 'jason', 'oniks', 'samantha']
names.insert(-1, 'raily')

ban_user = ['tulits', 'oniks' ]
ban_user.append('jason')


login = input('\nPls login your name: ').lower() #all input are transformed to lowercase
#for BAN USER
for name in names:
    if login == 'tulits': #TODO: I WANT TO USE THE 'BAN_USER' HERE BUT ITERATION TRU LIST NOT WORKING
        print(login + ( ' Not ALLOwED to enter'))
        break # stop Iteration if condition is TRUE
    else:
        print(login + (' Welcome to METAVERSE!'))
        break # stop Iteration


