import json

with open("data.json") as f:
    weather = json.load(f)
#print(weather)

#print(json.dumps(weather, indent=4))

print(40 *'#')
print(weather['name'])
print(10 * '-')
print(weather['weather'][0]['main'])
print('{:20} {}C'.format('Current temerature:', weather['main']['temp']))
print('{:20} {}C'.format('Minimum temperature:', weather['main']['temp_min']))
print('{:20} {}C'.format('Maximum temperature:', weather['main']['temp_max']))
#print('Maximum temperature: {}'.format(weather['main']['temp_max']))
print('{:20} {}m/s'.format('Wind speed:', weather['wind']['speed']))
#print('Wind speed:{}'.format(weather['wind']['speed']))
print(40 *'#')


################# engeto riesenie:

import json
f = open('data.json')
content = f.read()
f.close()
json_dict = json.loads(content)
city = json_dict.get('name')
weather = json_dict.get('main')
condition = json_dict.get('weather')[0].get('main')
curr_temp = str(weather.get('temp'))
max_temp =  str(weather.get('temp_max'))
min_temp =  str(weather.get('temp_min'))
wind_speed = str(json_dict.get('wind').get('speed'))
data = {'Current temperature': curr_temp + ' C', 'Minimum temperature': min_temp + ' C',
'Maximum temperature': max_temp + ' C', 'Wind speed': wind_speed + ' m/s'
 }
border = '#'*28
header = city + '\n' + '-'*14 + '\n'
cont = border + '\n' + header + '\n' + condition + '\n'
for d in data.items():
    cont += '{:20} {}\n'.format(*d)
cont += border
print(cont)
