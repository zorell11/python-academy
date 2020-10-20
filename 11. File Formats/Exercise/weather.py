import json

file = open('weather.json', 'r')
content=json.load(file)
file.close()
info = ['Current temerature:', 'Minimum temperature:', 'Maximum temperature:', 'Wind speed:']
max = 0
for i in info:
    if len(i) > max:
        max = len(i)
print(max)


print(len)
print(28 * '#')
print(content['name'])
print(13 * '-')
print(content['weather'][0]['main'])
print('{} {}'.format(info[0], content['main']['temp']))
print('{} {}'.format(info[1], content['main']['temp_min']))
print('{} {}'.format(info[2], content['main']['temp_max']))
print('{} {}m/s'.format(info[3], content['wind']['speed']))
print(28 * '#')
