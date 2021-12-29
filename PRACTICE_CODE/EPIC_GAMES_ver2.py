#
#
# EPIC GAMES 2021 Part 2
games = ['valorant', 'league of legends', 'final fantasy', 'beat saber', 'the las of us']
price_of_games = [1500, 800, 2300, 500, 2500]
number_of_game_sold = [1000, 5000, 500, 2000, 2500]

total_price_all_games = 0

for price in price_of_games:
  total_price_all_games = total_price_all_games + price

# print(total_price_all_games)
avr_price = total_price_all_games / (len(price_of_games))
# print(int(avr_price))
# print(price_of_games)
new_price = [n - 5 for n in price_of_games ]
# print(new_price)

def search_game(gamex,list):
    x = [gamex for game]

