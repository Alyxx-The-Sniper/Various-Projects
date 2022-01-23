# Hi This code will compute the Aircon Horse Power needed
# in a certain area.

#Gathering Data
roomsize = int(input('Input Room Size: in square meter\n'))
people = int(input('Number of people usually in the room:\n'))
directhit = (input('Does the room receive direct hit from the Sun? yes or no\n'))
window = input('Are the windows shaded? yes or no\n')

#Variables and their BTU equialent/multiplier
one_sqm = 750
one_person = 600
directhit_no = 1
directhit_yes = 1.2
window_shaded_yes = 1
window_shaded_no = 1.3
one_hp = 9000
one_point_five_hp = 12000
two_hp = 18000
two_point_five_hp = 22500
three_hp = 27000


#Function
def compute_aircon_horsepower(Room_size,Number_of_people_usually_in_the_room,):
    area_btu = Room_size * one_sqm
    people_btu = Number_of_people_usually_in_the_room * one_person

    total_btu = area_btu + people_btu

    return  total_btu



##############################################################################################
#SCENARIO ONE
if directhit == 'yes' and window == 'yes':
    hp = (compute_aircon_horsepower(roomsize, people) * directhit_yes * window_shaded_yes)
    if hp <= one_hp:
        print('You need 1.0 hp Aircon')
    elif hp <= one_point_five_hp:
        print('You need 1.5 hp Aircon')
    elif hp <= two_hp:
        print('You need 2.0 hp Aircon')
    elif hp <= two_point_five_hp:
        print('You need 2.5 hp Aircon')
    elif hp <= three_hp:
        print('You need 3.0 hp Aircon')
    else:
        print('\nFor Higher Aircon Capacity, Pls Contact Aircon Specialist')
#########################################################################################
#SCENARIO TWO
if directhit == 'yes' and window == 'no':
    hp = (compute_aircon_horsepower(roomsize, people) * directhit_yes * window_shaded_no)
    if hp <= one_hp:
        print('You need 1.0 hp Aircon')
    elif hp <= one_point_five_hp:
        print('You need 1.5 hp Aircon')
    elif hp <= two_hp:
        print('You need 2.0 hp Aircon')
    elif hp <= two_point_five_hp:
        print('You need 2.5 hp Aircon')
    elif hp <= three_hp:
        print('You need 3.0 hp Aircon')
    else:
        print('\nFor Higher Aircon Capacity, Pls Contact Aircon Specialist')
#########################################################################################
#SCENARIO THREE
if directhit == 'no' and window == 'yes':
    hp = (compute_aircon_horsepower(roomsize, people) * directhit_no * window_shaded_yes)
    if hp <= one_hp:
        print('You need 1.0 hp Aircon')
    elif hp <= one_point_five_hp:
        print('You need 1.5 hp Aircon')
    elif hp <= two_hp:
        print('You need 2.0 hp Aircon')
    elif hp <= two_point_five_hp:
        print('You need 2.5 hp Aircon')
    elif hp <= three_hp:
        print('You need 3.0 hp Aircon')
    else:
        print('\nFor Higher Aircon Capacity, Pls Contact Aircon Specialist')
#########################################################################################
#SCENARIO FOUR
if directhit == 'no' and window == 'no':
    hp = (compute_aircon_horsepower(roomsize, people) * directhit_no * window_shaded_no)
    if hp <= one_hp:
        print('You need 1.0 hp Aircon')
    elif hp <= one_point_five_hp:
        print('You need 1.5 hp Aircon')
    elif hp <= two_hp:
        print('You need 2.0 hp Aircon')
    elif hp <= two_point_five_hp:
        print('You need 2.5 hp Aircon')
    elif hp <= three_hp:
        print('You need 3.0 hp Aircon')
    else:
        print('\nFor Higher Aircon Capacity, Pls Contact Aircon Specialist')
from time import *
sleep(10)
############# THANK YOU .. ;) #########################################################

# testing commit change 12/18/21 - by toto
















