#
#
#
#
rank = ['mythic', 'epic', 'mythic', 'epic', 'barbarian' ]
name = ['alex', 'baron', 'kino', 'oika', 'tulits']

search_by_rank = input('\nSearch by Rank: ')

for (r,n) in zip(rank,name):
    while r == search_by_rank:
        print(r + ' = ' + n)
        break
