def weather_condition(temperature):
    if temperature > 20:
        return 'Warm'
    else:
        return 'Cold'

user_input = input('Enter temperature: ')
temp = float(user_input)

print('It is', weather_condition(temp).lower(), 'now.')



