#
#
#
#
# Number of Return = Number of  variable
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_forecast(weather):
    first_day = " Tomorrow the weather will be " + weather[0]
    second_day = " The following day it will be " + weather[1]
    third_day = " Two days from now it will be " + weather[2]
    extra_day = " Extra days from now it will be " + weather[-1]

    return first_day, second_day, third_day, extra_day

monday, tuesday, wednesday, extra = threeday_weather_forecast(weather_data)

print(monday)
print(tuesday)
# print(wednesday)
# print(extra)

def 