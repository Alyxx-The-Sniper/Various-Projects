#
#
#
#
#
#Airdrops
#token holders above 160 will get 50% increase and below will get nothing

holders_name = ['alex', 'baron', 'kino', 'oika', 'tulits']
token_amounts = [161, 164, 156, 144, 190,]

output_eligible = [( h, (t * 1.5)) for h,t in zip(holders_name, token_amounts) if t > 160]
output_non_eligible = [(h, (t * 1)) for h,t in zip(holders_name, token_amounts) if t <= 160]

output_all = output_eligible + output_non_eligible

# print(output_eligible)
# print(output_non_eligible)
# print(output_all)



