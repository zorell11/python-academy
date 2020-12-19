import json

f = open('pocasie.json')
data = json.load(f)
f.close()

print(data[0].get("address_components").get("short_name"))
teplota = []
for i in data[0]["weather"]["temperature"].values():
    teplota.append(i)
print('{} °C | {} °C | {} °C'.format(*teplota))

if data[0]["weather"]["rain"]["raining"] == True:
    print('//')


vietor = []
for i in data[0]["weather"]["wind"].values():
    vietor.append(i)
print('Směr větru: {}'.format(vietor[0]))
print('Rychlost větru: {}m/s'.format(vietor[1]))
