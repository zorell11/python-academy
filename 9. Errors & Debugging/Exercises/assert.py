def avg(lst):
    # Testujeme jestli funkce nedostala prázdný list.
    assert len(lst) > 0, 'Potřebuji neprázdný list.'
    return sum(lst) / len(lst)

print(avg([2]))
