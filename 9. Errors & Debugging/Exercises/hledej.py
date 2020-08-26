# V tomto úkolu budeš opět vytvářet funkci, tentokrát s názvem hledej.
#Tato funkce bude ve slovníku vyhledávat zadanou hodnotu u zadaného klíče. Funkce by měla:
# -brát 3 argumenty: hledaný klíč, hledanou hodnotu a prohledávaný slovník (kvůli testům prosím zvol argumenty v tomto pořadí!),
# -zkusit ve slovníku najít zadaný klíč,
# -pokud je klíč nalezen, funkce by měla zkontrolovat, zda hodnota souhlasí. Pokud ano, funkce vrátí True. Pokud ne, vrátí False,
# -pokud klíč není nalezen, funkce vypíše zprávu a vrátí hodnotu False.

muj_slovnik = {
    'jmeno':'Pepa',
    'prijmeni': 'Novak',
    'rok_narozeni': 1990,
    'mesto': 'Praha',
    'domaci_mazlicek': 'Chameleon'
}



def hledej(key, value, dict):
    if key in dict.keys() and dict[key] == value:
        return True
    elif dict[key] in dict.keys():
        return False
    else:
        print('Key not found in dictionary')
        return False


print(hledej('jmeno', 'Pepa', muj_slovnik))


def hledej(key, value, dict):
    try:
        if dict[key] == value:
            return True
        else:
            return False
    except KeyError:
        print('Key not found in dictionary')
        return False



hledej('jmeno', 'Pepa', muj_slovnik)
