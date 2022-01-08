


# SAMPLE PROJECT FOR VIKINGS RESTAURANT AND ALOHA COFFEE

class Business:

    def __init__(self, name, franchises_list ):
        self.name = name
        self.franchises = franchises_list



class Franchise:

    def __init__(self, name, address, menus):
        self.name = name
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.name + ' ' + self.address


    def available_menu(self, time):                             # Pls use military time
        menus = []                                              # I haven't imported 'time module' in this project

        if self.name == 'aloha coffee main':                    # Check first if franchise is aloha coffee main if TRUE
            if time not in range(101,1500):                     # priorities this condition
                menus.append(aloha_coffee_menu)
            return menus

        else:

            for i in all_menu:                                   # Iterate through 'all_menu' [brunch, early_bird, dinner,kids]
                if time >= i.start_time and time <= i.end_time:  # example, i.start_time  = print(brunch.start_time)
                    menus.append(i)
            return menus



class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def calculate_bill(self, purchase_items_list): # ==> brunch.calculate_bill([purchase_items_list]) <- type list
        bill = 0
        # print('List Of Purchase:')
        for purchase_item in purchase_items_list:
            if purchase_item in self.items: # current object.items
                bill += self.items[purchase_item]
            #     a = purchase_item
            #     b = self.items[purchase_item]
            #     print( a + ': ' + str(b) )
            #
            # else:
            #     purchase_item not in self.items
            #     print('"' + purchase_item + '"' + ' Not available in ' + self.name + ' Menu')

        return bill


    #Representation of object and time_start and time_end
    def __repr__(self):
        return self.name + ' is available from ' + str(self.start_time) + ' - ' + str(self.end_time)





#########################################################################################################
# LIST OF ITEMS
# You can add/delete or edit items HERE!!!

# FOR VIKINGS
brunch_menu_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,
                     'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50,
                     'orange juice': 3.50}
early_bird_menu_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                         'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
                         'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
dinner_menu_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00,
                     'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50,
                     'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
kids_menu_items ={'chicken nuggets': 6.50,
                  'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
all_menu_content_vikings = [brunch_menu_items, early_bird_menu_items, dinner_menu_items, kids_menu_items]


# FOR ALOHA COFFEE (NEW BUSINESS)
coffee_menu_items = {'americano': 7.00, 'mocha': 8.50,
                    'barako': 8.00, 'cafelatte': 7.50}







#########################################################################################################

# CLASS MENU
# objects/instance of the class

# FOR VIKINGS
brunch = Menu('brunch', brunch_menu_items, 1100, 1600)
early_bird = Menu('early_bird', early_bird_menu_items, 1500, 1800)
dinner = Menu('dinner', dinner_menu_items, 1700, 2300)
kids = Menu('kids', kids_menu_items, 1100, 2100)
all_menu = [brunch,early_bird,dinner,kids]


# FOR ALOHA COFFEE
aloha_coffee_menu = Menu('aloha coffee menu', coffee_menu_items, 1500, 100)
#
#
#



#########################################################################################################

# CLASS FRANCHISE
# Create a Franchise HERE!!!

# FOR VIKING BUSSINESS
viking_main = Franchise('vikings main', "1232 West End Road", all_menu)
viking_branch1 = Franchise('vikings branch1', "12 East Mulberry Street", all_menu)
# branch2 soon...
# branch3 soon...
# branch4 soon...
vikings_all_franchises = [viking_main, viking_branch1]


# FOR ALOHA COFFEE
aloha_coffee_main = Franchise('aloha coffee main', 'antipolo city', aloha_coffee_menu)





#########################################################################################################

# CLASS BUSINESS

# Create Bussiness HERE!!!
vikings = Business('vikings', vikings_all_franchises)
aloha_coffee = Business('aloha coffee', aloha_coffee_main)







#########################################################################################################

# TESTING AREA!!

##################
#  Class Menu
#  brunch, early_bird, dinner, kids, aloha_coffee_menu --> (objects)
# .name / .item / .start_time / .end_time --> (attributes)
# .calculate_bill --> (methods)
#  Start Here

# print(brunch.items)
# print(dinner.start_time)
# print(aloha_coffee_menu.items)
# print(aloha_coffee_menu.calculate_bill(['americano', 'mocha']))






##################
#  Class Franchise
#  viking_main, viking_branch1, aloha_main --> (objects)
# .address /.menus --> (attributes)
# .available_menu  --> (methods)
#  Start Here

# print(viking_main.menus)
# print(viking_branch1.available_menu(100))
# print(viking_branch1.available_menu(1100))

# print(aloha_coffee_main.address)
# print(aloha_coffee_main.menus)
# print(aloha_coffee_main.available_menu(100))
# print(aloha_coffee_main.available_menu(101))
# print(aloha_coffee_main.available_menu(2400))







##################
#  Class Business
#  vikings, aloha coffee  --> (objects)
# .name / .franchises     --> (attributes)
#  Start Here

# print(aloha_coffee.franchises)
# print(vikings.franchises)




