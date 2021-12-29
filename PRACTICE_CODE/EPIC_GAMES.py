#
#
# EPIC GAMES 2021
games = ['valorant', 'league of legends', 'final fantasy 1', 'beat saber', 'the las of us']
price_of_games = [1500, 800, 2300, 500, 2500]
number_of_game_sold = [1000, 5000, 500, 2000, 2500]




#############################################################
#############################################################
def game_name_edit(original, edited):
    for i in range(len(games)):
        if games[i] == original:
            games[i] = edited
            return games
            break #Once condition is TRUE break loop
        else:
            return games
            break #Once condition is TRUE break loop


print(game_name_edit('valorant', 'valorante'))
#############################################################
#############################################################
#############################################################
#############################################################
def edit_game_price(game, new_p):

    index = games.index(game)
    new_price_of_games = price_of_games[ :index ] #slice price_of_games for append preparation
    new_price_of_games.append(new_p)
    new_price_of_games = new_price_of_games + price_of_games[ index +1 :  ]
    return new_price_of_games


print(edit_game_price('valorant', 999)) #TODO: Error handling for input games that are not in the list
#############################################################
#############################################################

















#################################

def add_game(game):
    games.append(game)
    return games

# def edit_games(g): TODO: how to edit element in a list
#def search























def add_price(price):
    price_of_games.append(price)
    return price_of_games

def add_sold(sold):
    number_of_game_sold.append(sold)
    return number_of_game_sold

add_game('final fantasy 2')
add_game('final fantasy 3')
































# #Christmas Discount league of legends 25% off
# # for index, game in enumerate(zip(games,price_of_games)): TODO: find another way to update element in a list
# #     print(index, game)
# # league of legend index value is 1, as per executing above code
# # lol_price = price_of_games[1]  #TODO: Create a function that search a game and edit its price
# # new_lol_price = int(lol_price * .75)
# # price_of_games.pop(1)
# # price_of_games.insert(1,new_lol_price)
#
#
#
#
#
#
#
#
#
#
#
# # print(list(zip(games,price_of_games)))
# # print(list(zip(games,price_of_games)))
#
#
#
#
#
#
#
#
#
#
#
# #League of legends has increase its sales record by 50% due to discount
# #We know already the index value of LOL which is 1
# lol_number_of_game_sold = number_of_game_sold[1]
# new_lol_number_of_game_sold = int(lol_number_of_game_sold * 1.5)
# number_of_game_sold.pop(1)
# number_of_game_sold.insert(1, new_lol_number_of_game_sold)
#
#
#
#
#
#
#
#
#
#
#
# #For update/revision pls code it above this line.
# #######################################################################
#
#
# game_and_price = zip(games, price_of_games)
# games_and_number_of_purchase = zip(games, number_of_game_sold)
# # print(list(game_and_price))
# # print(list(games_and_number_of_purchase))
#
# sales_per_game = [(p * n) for p, n in zip(price_of_games, number_of_game_sold)]
# # print(sales_per_game)
#
#
# #######################################################################
# #top 3 games per total games sold
# games_and_number_of_sold_zip = zip(number_of_game_sold, games)
# games_and_number_of_sold = list(games_and_number_of_sold_zip)
# games_and_number_of_sold.sort(reverse=True)
# top_3_games_based_on_sold = games_and_number_of_sold[:3]
#
# # print(top_3_games_based_on_sold)
#
# #######################################################################
# #top 3 games per total sales
# games_and_total_sales_zip = zip(sales_per_game,games)
# games_and_total_sales = list(games_and_total_sales_zip)
# games_and_total_sales.sort(reverse=True)
# top_3_games_based_on_sale = games_and_total_sales
#
# # print(top_3_games_based_on_sale[:3])
#
# #######################################################################
# #games with the lowest sales
# games_with_lowest_sale = top_3_games_based_on_sale[-1:]
# # print(games_with_lowest_sale)







