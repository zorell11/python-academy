def suma(lst):
    # Vytváříme proměnou pro výsledek.
    vysledek = 0
    for i in lst:
        # Načítáme obsah listu.
        vysledek += i
    # Vracíme výsledek.
    return vysledek
def prvky(lst):
    # Vytváříme proměnou pro výsledek.
    pocet_prvku = 0
    for i in lst:
        # Načítáme počet prvků
        pocet_prvku += 1
    # Vracíme výsledek.
    return pocet_prvku
def prumer(lst):
    # Vracíme výsledek předchozích funkcí.
    return suma(lst) / prvky(lst)
# Testovací listy.
list1 = list()
list2 = [1,2,'a', 55]
list3 = [1, 2, 3, 4, 5]
# Zkoušíme to všechno spustit.
try:
    # Sem si postupně vyzkoušej dát: list1, list2 a list3
    prumer_listu = prumer(list2)
    print(prumer_listu)
# Odchytáváme dělení nulou.
except ZeroDivisionError:
    # Vypisujeme zprávu.
    print('Jejda, někde dělíme nulou, nejspíš si zadal prázdný list.')
# Odchytáváme chybu při sčítání.
except TypeError:
    # Vypisujeme zprávu.
    print('Do tvého listu se vloudila nějaká nezbedná data.')
