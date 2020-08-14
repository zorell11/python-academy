# We have a dictionary:

film = {'name':'Forrest Gump',
        'made':1994,
        'director':'Robert Zemeckis',
        'soundtrack':'Multiple',
        'starring':'Tom Hanks',
        'fun_fact':'''The house used in Forrest Gump is the same house used in The Patriot (2000). Some paneling was changed
                    for interior shots  in the latter
                    film.'''}
#Create a script that will print each key - value pair to the terminal in format:
# "Key: <key> | Value: <value>"
#Example of running the script:
#$ python3 list_items.py
#Key: starring | Value: Tom Hanks
#Key: director | Value: Robert Zemeckis
#Key: made | Value: 1994
#Key: name | Value: Forrest Gump
#Key: soundtrack | Value: Multiple
#Key: fun_fact | Value: The house used in Forrest Gump is the same house used in The Patriot (2000). Some paneling was changed for interior shots in the latter film.

key = list(film.keys())
value = list(film.values())
number = 0
while number < len(key):
    print('Key:', key[number], '| Value:', value[number])
    number += 1
