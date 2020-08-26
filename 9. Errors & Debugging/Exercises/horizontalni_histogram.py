# Nyní bude tvým úkolem vytvořit funkci horizont_hist(), která vezme list čísel jako
#argument a na základě hodnot v tomto listu vytiskne histogram v terminálu.
#Výška sloupce by měla odpovídat hodnotě odpovídajícího čísla v listu


def horizont_hist(lst):
    for i in lst:
        print('|{:}'.format(i*'*'))


print(horizont_hist([4,5,7,10,6,3,2]))
