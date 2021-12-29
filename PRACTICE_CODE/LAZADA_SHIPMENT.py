
#LAZADA
#This will calculate the shipping cost per shipment method
#
#########################################################################
#   Sea Shipment ((flat charge + ( Weight * Price per Pound))
#   Weight of Package	        Price per Pound	Flat       Flat Charge
#   => 2 lb                        $1.50                	$20.00
#   < 2 lb but => 6 lb	           $3.00	                $20.00
#   < 6 lb but => 10 lb	           $4.00                	$20.00
#   < 10 lb	                       $4.75	                $20.00
##########################################################################
#   Air Shipment ((flat charge + ( Weight * Price per Pound))
#   Weight of Package	        Price per Pound	Flat       Flat Charge
#   => 2 lb                        $4.50                	$20.00
#   < 2 lb but => 6 lb	           $9.00	                $20.00
#   < 6 lb but => 10 lb	           $12.00                	$20.00
#   < 10 lb	                       $14.25	                $20.00
##########################################################################

packageName = input('\nWhat is in the Package?: ')
packageWeight =int(input('Weight of the Package (lbs): '))


#######################################################################
# Statement for SEA Shipment
if packageWeight <= 2:
    costSea = packageWeight * 1.5 + 20
elif packageWeight <= 6:
    costSea = packageWeight * 3 + 20
elif packageWeight <= 10:
    costSea = packageWeight * 4 + 20
elif packageWeight > 10:
    costSea = packageWeight * 4.75 + 20
# Put Error Handling Here :TODO must put Error Handling Code Here!

print('\n     SEA Shipment Cost ' + str(costSea) + '$ Dollar')

#######################################################################
# Statement for AIR Shipment
if packageWeight <= 2:
    costAir = packageWeight * 4.5 + 20
elif packageWeight <= 6:
    costAir = packageWeight * 9 + 20
elif packageWeight <= 10:
    costAir = packageWeight * 12 + 20
elif packageWeight > 10:
    costAir = packageWeight * 14.25 + 20
# Put Error Handling Here :TODO must put Error Handling Code Here!

print('     AIR Shipment Cost ' + str(costAir) + '$ Dollar')









