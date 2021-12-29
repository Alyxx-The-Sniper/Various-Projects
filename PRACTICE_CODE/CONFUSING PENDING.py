


weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']


def threeday_weather_report(weather):
    first_day = " Tomorrow the weather will be " + weather[0]
    second_day = " The following day it will be " + weather[1]
    third_day = " Two days from now it will be " + weather[2]
    tup = [first_day,second_day,third_day]
    return tup

monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)

x, y, z = 1, 2, 3,
[a,b,x] = [11,22,33]
print(y,z)
print(x)