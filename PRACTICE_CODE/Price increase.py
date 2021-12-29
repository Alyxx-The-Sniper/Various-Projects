#
#
#
#
items = ['carrot', 'potato', 'onion', 'chili', 'garlic']
prices = [10, 20, 5, 3, 2]

item_and_price = (zip(items,prices))
old_price = list(item_and_price)

#Price increase 100%
new_price = []
for (i,p) in zip(items,prices):
    variable1 =  (i, p * 2)
    new_price.append(variable1)

print(old_price)
print(new_price)



