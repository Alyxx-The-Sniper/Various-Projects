#
#
#
#
def f_to_c (f_temp):
    return ((f_temp -32) * 5/9)
    #
    # c_temp = ((f_temp -32) * 5/9)
    # print(c_temp)

room1 = f_to_c(72)
room2 = f_to_c(100)
room3 = f_to_c(50)


###############################################################################
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

###############################################################################
def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(100,150)
# print('The GE train supplies ' + str(train_force) +  ' Newtons of force')



###############################################################################
def get_energy(mass, c = (3 * (10**8))):
    return mass * (c**2)

bomb_energy = get_energy(1)
# print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules')



###############################################################################
def get_work(mass, acceleration, distance):
    force = get_force(mass,acceleration)
    return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print(train_work)
